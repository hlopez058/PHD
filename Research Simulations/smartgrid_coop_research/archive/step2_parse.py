import pandas as pd
import requests
import os
import pathlib
import step1_raw as step1
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Parsing raw data into data frame
def eia_parse(df):
    #remove any empty values
    df.dropna(subset=['generation'], inplace=True)
    df.dropna(subset=['demand'], inplace=True)

    #normalize the dataset
    gen_max = max(df['generation'])
    dem_max = max(df['demand'])
    df['generation'] = df['generation'].apply(lambda x: x/gen_max)
    df['demand'] = df['demand'].apply(lambda x: x/dem_max)

    # group the hourly values into monthly?
     
    print("Step 2: Data wrangling completed.")

    return df

def test(df):
    
    df = eia_parse(df)

    # Demand curve as a normalized value
    N = max(df['demand'])
    samples = len(df['demand'])
    x = np.linspace(0, samples,samples)
    y = df['demand'] * (1100/730)

    
    # fit a linear curve an estimate its y-values and their error.
    y_err = 2 * y.std()

    fig, ax = plt.subplots()
    ax.plot(y, '-')
    ax.fill_between(x,y - y_err, y + y_err, alpha=0.2)
    ax.plot( y, '-', color='brown')
  

    # group by 24
    size=24
    list_of_dfs = (df.loc[i:i+size-1,:] for i in range(0, len(df),size))
    agg_data = []
    for ldf in list_of_dfs:
      agg_data.append(ldf['demand'].sum()*(1100/730))
    
    y = np.array(agg_data)
    samples = len(y)
    x = np.linspace(0, samples,samples)
    fig, ax = plt.subplots()
    y_err = 2 * y.std()
    ax.plot(y, '-')
    ax.fill_between(x,y - y_err, y + y_err, alpha=0.2)
    ax.plot( y, '-', color='green')


    # group by 24
    size=24
    list_of_dfs = (df.loc[i:i+size-1,:] for i in range(0, len(df),size))
    agg_data = []
    for ldf in list_of_dfs:
      agg_data.append(ldf['generation'].sum()*(10))
    
    y = np.array(agg_data)
    samples = len(y)
    x = np.linspace(0, samples,samples)
    fig, ax = plt.subplots()
    y_err = 2 * y.std()
    ax.plot(y, '-')
    ax.fill_between(x,y - y_err, y, alpha=0.2)
    ax.plot( y, '-', color='orange')

    #plt.show()