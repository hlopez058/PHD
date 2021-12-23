import requests
import pandas as pd
from functools import reduce
from numpy import random
import numpy as np
import os
import pathlib
from datetime import datetime
from multiprocessing import Process
from multiprocessing import Pool,Value
import time

# dataframe
eia_data_curves = None
settings_size = 0
counter = Value('i', 0)

def main():
    sweep_settings = {
        "number_of_prosumers" : 500,
        "dem_mean_sweep_kWh_mo" : np.arange(800,1500,100),
        "gen_mean_sweep_kWh_mo" : np.arange(800,1500,100),
        "gen_var_sweep" : np.arange(0.1,0.3,0.1),
        "dem_var_sweep" : np.arange(0.1,0.3,0.1)
    }   

    prosumer_data = []
    settings = get_swept_settings(sweep_settings)
    
    global settings_size 
    settings_size = len(settings)
    print(f"Length of settings {settings_size}")

    print("generated the swept settings to build")
    
    start_time = datetime.now()
    with Pool(20) as p:
        prosumer_data.extend((p.imap_unordered(f, settings, 1000)))
        print(f"completed {len(prosumer_data)} of {len(settings)}")
    end_time = datetime.now()

    print('Duration: {}'.format(end_time - start_time))

    print("building file")
    prosumer_df = pd.concat(prosumer_data)
    curr_path = os.path.abspath(os.path.dirname(__file__))
    prosumer_df.to_csv(f"{curr_path}/data/prosumer_N{sweep_settings['number_of_prosumers']}_all_{datetime.today().strftime('%Y%m%d_%H')}.csv",index=False)
    print("done")

def f(setting):
    global settings_size
    global counter
    with counter.get_lock():
        counter.value += 1
    print(f"{counter.value} out of {settings_size}")
    p = Prosumer(id=setting['id'],df=eia_data_curves,setting=setting).data
    return p    


def get_data(path,query):
    df = pd.read_csv(path) 
    # fix the timestamp format 
    df["time"] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M')
    df.sort_values(by='time')
    # place id at head of table
    first_col = df.pop('id')
    df.insert(0, 'id', first_col)
    # select for specific values
    df.query(query,inplace=True)
    #get only a selected amount of users
    return df

def get_swept_settings(sweep_settings):
    N = sweep_settings['number_of_prosumers']
    settings = []
    uid = 0
    for n in range(N):
        print(f"\tcreating settings for {n} of {N}")
        for dem_mean in sweep_settings['dem_mean_sweep_kWh_mo']:
            for gen_mean in sweep_settings['gen_mean_sweep_kWh_mo']:
                for gen_var in sweep_settings['gen_var_sweep']:
                    for dem_var in sweep_settings['dem_var_sweep']:
                        setting = {
                                    'uid':uid,
                                    'id':n+1,
                                    'dem':
                                        {
                                            'type':'demand',
                                            'mean':dem_mean,
                                            'std': dem_mean * dem_var, #20% of mean
                                            'ulim':dem_mean * 1.5, # upper limit (max load),
                                            'llim':dem_mean * 0.05 # lower limit (constant load) 
                                        },
                                    'gen':
                                        {
                                            'type':'generation',
                                            'mean':gen_mean,
                                            'std': gen_mean * gen_var, #20% of mean,
                                            'ulim':gen_mean, # upper limit (capacity),
                                            'llim':0, # lower limit
                                        } 
                                    }
                        settings.append(setting)
                        uid = uid+1
    return settings

def get_EIA_Datasets():
    # set settings for EIA api
    eia_api_config = {
        "start" :'201910',
        "end" : '202012',
        "url" : 'http://api.eia.gov/series/',
        "api_key" :'d42ebe76b736d7815489e3298ff17079'
    }
    # call each dataset from api and capture into dataset object
    dataset_demand = Dataset(name='demand',query='ELEC.SALES.FL-RES.M',config=eia_api_config) 
    dataset_generation = Dataset(name='generation',query='ELEC.GEN.DPV-FL-8.M',config=eia_api_config)
    dataset_price = Dataset(name='price',query='ELEC.PRICE.FL-RES.M',config=eia_api_config)
    dataset_demand.convert(pow(10,6))
    dataset_generation.convert(pow(10,6))
    dataset_demand.normalize()
    dataset_generation.normalize()
    # merge the datasets by time column
    df = reduce(lambda left,right: pd.merge(left,right,on=['time'],how='outer'), [dataset_demand.df , dataset_generation.df, dataset_price.df])
    return df

# Data Gathering Settings
class Dataset:
    def __init__(self, name, query,config):
        self.name = name
        self.query = query
        self.config = config
        self.df = self.fetch()
    def convert(self,unit):
        self.df[self.name] = self.df[self.name].apply(lambda x: x*unit)
    def normalize(self):
        self.df[self.name] = self.df[self.name].apply(lambda x: x/self.df[self.name].max())
    def fetch(self):
        full_url = f"{self.config['url']}?api_key={self.config['api_key']}&series_id={self.query}&start={self.config['start']}&end={self.config['end']}"
        data = requests.get(full_url).json()['series'][0]['data']
        df = pd.DataFrame(data,columns=['time',self.name])
        df['time'] =  pd.to_datetime(df['time'], format='%Y%m')
        return df

class Prosumer:
    def __init__(self, id, df, setting):
        self.id = id
        gen = self.get_random_curve(setting=setting['gen'],curve=df[['time','generation']])
        dem = self.get_random_curve(setting=setting['dem'],curve=df[['time','demand']])
        price = df[['time','price']]
        diff = dem['demand'] - gen['generation']
        consumption = pd.DataFrame(list(zip(gen['time'],[max(x,0) for x in diff])),columns=['time','consumption'])
        net_energy = pd.DataFrame(list(zip(gen['time'],[min(x,0) for x in  diff])),columns=['time','net_energy'])
        self.data = reduce(lambda left,right: pd.merge(left,right,on=['time'],how='outer'), [dem, gen, consumption, net_energy,price])
        self.data["id"] = self.id
        self.data['demand_std'] = setting['dem']['std'] 
        self.data['generation_std'] = setting['gen']['std'] 
        self.data['generation_mean'] = setting['gen']['mean']
        self.data['demand_mean'] = setting['dem']['mean']
        
    # Given statistical arguments , converts an original dataframe curve with 'time' value and col of setting['type'] to
    # randomly sampled equivalent given the setting['std'],setting[llim],setting[ulim],setting['mean'] values.
    def get_random_curve(self,setting,curve):
        c = [max(setting['llim'],min(setting['ulim'],random.normal(loc=setting['mean'],scale=setting['std'])*x)) for x in curve[setting['type']]]
        return pd.DataFrame(list(zip(curve['time'],c)),columns=['time',setting['type']])



def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

if __name__ == "__main__":
    # execute only if run as a script
    info('main line')

    eia_data_curves = get_EIA_Datasets()
    settings_size = 0
    print("collected data from eia.gov api")

    main()