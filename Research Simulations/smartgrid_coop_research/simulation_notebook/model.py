from pandas import read_csv
from matplotlib import pyplot
# load the dataset
dataframe = read_csv(
    "/Users/HXL0TP5/Repos/PHD/Research Simulations/smartgrid_coop_research/simulation_notebook/data/prosumer_N50_all_20210409_00.csv", header=0)
df_by_id = dataframe[["time", "price", "id"]].groupby("id")
for df in df_by_id:
    print(df[1][["time", "price"]].values)
    #data = df[["time", "price"]].values
    # choose the input and output variables
    #x, y = data[:, 0], data[:, 1]
    #print(x, y)
    # plot input vs output
    #pyplot.scatter(x, y)
    # pyplot.show()
