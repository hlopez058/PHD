import pandas as pd
import numpy as np
####################################################################
# Data Gathering
####################################################################
# Data gathering and synthesization has been done in a seperate module.
# import the external data gathering set. Pull data from a dataset 
# of randomly insantiated prosumer, synthesized from EIA.gov data trends
# 
import p0_data_gather as p0

####################################################################
# get dataset by calling the local file and queirying for 
# parameters desired. 
# database : path of the dataset 
# query : dictionary of values
# {
#   "N" : 3
#   "demand" : 1100,
#   "generation" : 1300,
#   "demand_variance" : 0.1,
#   "generation_variance" : 0.1
#    
# }
# Returns:
# Dictionary : {
#   N : number of prosumers
#   df : eia_dataset dataframe
#   df_by_t: [] of daframes split by time col 
# }
#
#
####################################################################
def get_eia_dataset(database,query):
    # Set path of dataset file containing all parameterized values
    data_set_path = database
    # Set initial conditions for prosumers dataset
    dem_mean = query['demand']
    gen_mean = query['generation'] 
    dem_std =dem_mean * query['demand_variance']
    gen_std = gen_mean * query['generation_variance']
    # Set number of prosumers, an array of N[] values for multiple experiments 
    if query['N'] is type(int):
        number_of_prosumers_for_each_trial = [query['N']]
    else:
        number_of_prosumers_for_each_trial = query['N']
    # Trials [] holds session data for each N itteration of prosumers
    eia_dataset_trials = []
    for N in number_of_prosumers_for_each_trial:
        # Call the data as a query with the instantiated values
        eia_dataset = p0.get_data(path=data_set_path,
        query=f"""id > 0 & id<={N} & demand_std == {dem_std} & generation_std == {gen_std} & generation_mean == {gen_mean} & demand_mean == {dem_mean}""")
        eia_dataset['net_energy'] = eia_dataset['generation'] - eia_dataset['consumption']
        # Data Wrangling : Split data by time 't'
        ####################################################################
        # Wrangle data into monthly timesteps then add to an object for each trial
        eia_dataset_by_t = [pd.DataFrame(y) for x, y in eia_dataset.groupby('time', as_index=False)]
        eia_trial = {"N":N, "df":eia_dataset,"df_by_t":eia_dataset_by_t}
        eia_dataset_trials.append(eia_trial)
    return eia_dataset_trials
