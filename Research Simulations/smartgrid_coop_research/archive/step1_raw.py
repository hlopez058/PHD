#import data from sources
import pandas as pd
import requests
import os
import pathlib
from pathlib import Path
from datetime import datetime

# Step 1 : Collecting raw data from source API
def eia_raw(args):
    print("Gathering data started.")
    d = Path(__file__).resolve()
    dir_data = os.path.join(str(d.parent),'data')
    data_input_filename = os.path.join(dir_data,args['data_file'])
    data_input_filename_daily = os.path.join(dir_data,args['daily_data_file'])
    start =args['start_date'] #YYYYMM
    end = args['end_date']
    
    if not os.path.exists(os.path.join(dir_data,data_input_filename)):
        print("Data not found calling API for new dataset.")
        api_key = args['api_key']
        eia_fpl_demand_url = f"http://api.eia.gov/series/?api_key={api_key}&series_id=EBA.FLA-ALL.D.H&start={start}&end={end}"
        eia_solar_generation_url = f"http://api.eia.gov/series/?api_key={api_key}&series_id=EBA.FLA-ALL.NG.SUN.H&start={start}&end={end}"
        eia_fpl_retail_price_url = f"http://api.eia.gov/series/?api_key={api_key}&series_id=ELEC.PRICE.FL-RES.M&start={start}&end={end}"
        
        r = requests.get(url = eia_fpl_demand_url)
        #print(r.json())
        eia_fpl_demand_data = r.json()['series'][0]['data']
        eia_fpl_demand_data_units = r.json()['series'][0]['units']

        r = requests.get(url = eia_solar_generation_url)
        eia_solar_generation_data = r.json()['series'][0]['data']
        eia_solar_generation_data_units = r.json()['series'][0]['units']
        
        r = requests.get(url = eia_fpl_retail_price_url)
        eia_fpl_retail_price_data = r.json()['series'][0]['data']
        
        df_demand =pd.DataFrame(eia_fpl_demand_data,columns=['time','demand'])
        df_generation =pd.DataFrame(eia_solar_generation_data,columns=['time','generation'])
        df_price = pd.DataFrame(eia_fpl_retail_price_data,columns=['time','price'])


        
        # TODO : merge the pricing into the same dataframe by looking at the month

        # TODO : embed units for each dataset

        #joined by time key
        df = df_generation.merge(df_demand, on ='time')
        df.to_csv(data_input_filename)
        
        df = rollup_hourly_to_daily(df)
        df.to_csv( data_input_filename_daily)
    
        print("Step 1: Data gathering completed.")
        return df
    else:
        # read file into dataframe
        df = pd.read_csv(data_input_filename) 
        df = rollup_hourly_to_daily(df)
        print("Step 1: Data gathering completed.")
        return df
    
    
    # monhtly retail pricing
    # http://api.eia.gov/series/?api_key=d42ebe76b736d7815489e3298ff17079&series_id=ELEC.PRICE.FL-RES.M

def rollup_hourly_to_daily(df):
    # roll up hourly into daily
    # create a time  list and convert to datetime object
    time_stamps = df['time']
    datetimes = []
    for t in time_stamps: 
        dt = datetime.strptime(t,'%Y%m%dT%HZ')
        r = {t,dt.strftime("%Y%m%d")}
        datetimes.append(r)

    df_date = pd.DataFrame(datetimes,columns=['time','date'])
    
    df = df.merge(df_date, on ='time')
    df = df.groupby(['date'])[['generation']].sum()
    return df

def test(args):
    df  = eia_raw(args)
    print(df)
    return df


