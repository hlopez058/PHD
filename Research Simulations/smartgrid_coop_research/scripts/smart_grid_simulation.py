# Derived from Application of cooperative game theory in smart grids
# Thesis reference by Vottem University of texas
# Simualtion of system model 4.1.1

import math
import random
import os
import csv

# Define Environment Variables as Globals?
Solar_Irradiance = [1,9,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]
Average_Consumer_Load = []

def main():
    # Build network of prosumers
    # Build network of conusmers
    # Build exchange functions
    # Build exchange market
    # Build NRG coin example
    #dso = DSO(1)
    #kwh = dso.Substations[0].Prosumers[0].Production(t=1)
    Average_Consumer_Load = LoadData.wrangle_fpl_load_curve_data("930-data-export.csv")

    print(o)

class DSO():
    def __init__(self,num_of_substations=1):
        """
        Distribute System operator
        Manages a series of substations
        """
        self.Substations = []
        for i in range(num_of_substations):
            self.Substations.append(Substation(id=i))

class Substation():
    def __init__(self,id,num_of_prosumers=1):
        """
        Electrical substation collects input energy
        calculates the total production and total 
        consumption of the connected prosumers
        """
        self.id = id
        self.Prosumers = []
        for i in range(num_of_prosumers):
            self.Prosumers.append(Prosumer(id=i))

        #self.tp = #sum of all prosumer production
        #self.tc = #sum of all prosumer consumption

    def g(self,x,n,q,tp,tc,a):
        """
        g(x,tp,tc) 
        payback distribution function
        based on NRGX-Change algorithm
        x : net input energy
        n : exponential rates for input energy
        q : max rate of return
        tp : total supply
        tc : total demand
        a : scaling factor
        """
        return (math.pow(x,n)*q) / (math.exp(math.pow(tp-tc,2)/a))
        
    def h(self,y,n,r,tp,tc):
        """
        h(y,tp,tc) 
        consumer cost of energy 
        based on NRGX-Change algorithm
        y : withdrawn energy
        n : exponential rates for withdrawn energy
        r : max rate of return
        tp : total supply
        tc : total demand
        """
        return (math.pow(y,n)*r*tc) / (tc+tp)

class Prosumer():
    def __init__(self,id):
        """
        A home that can consume and
        produce energy from a local power 'Plant'
        with some capacity limit
        """
        self.id = id
        self.Plant = Plant(type ='solar',capacity = 500)
    def Production(self, t):
        """
        Return production in kWh at some time 't'
        """
        return self.Plant.output(t)
    def Consumption(self,t):
        """
        Return consumption of prosumer home based on
        residential consumption model
        """
        average_load = 877/730 # 877 kWh per month
        return average_load

class Plant():
    def __init__(self,type,capacity):
        """
        A plant generates energy and 
        provides it as an output energy
        for a prosumer
        """
        self.type = type
        self.capacity = capacity
    def output(self, t):
        """
        Output of the plant at time 't'
        """
        return random.randint(0,Solar_Irradiance[t]*self.capacity)

class LoadData():
    def __init__(self):
        pass
    # Demand Curve Sample Data Methodology
    # ---------------------------------------------------------
    # Data from FPL eia.gov tools 
    # FPL's service territory includes over 4.6 million customers
    # Sample data of 11/20/20 to 11/27/20 by hour of consumer demand
    # Using the real demand curves we can estimate consumer demand
    # by Household. In Florida, a survey (https://www.floridarealtymarketplace.com/blog/how-much-power-does-a-house-use.html#:~:text=In%20Florida%2C%20the%20survey%20showed,windows%2C%20doors%2C%20and%20roofs.)
    # showed that the average home used 1,110 kWh (~14k kwh/yr) . 
    # This can be used to estimate 
    # (4.6M * 1110kWh/mo) / 730 = Total FPL Demand in kWh
    # 6,000 MWh on average. The max of the data demand is 18k MWh 
    # with an average of 12000 MWh. By cutting the demand from the
    # sample data set in half we can safely assume that the 
    # remaining clients would be commercial and ancillary loads
    # with the reasoning that the average home would be 1000kWh
    # fields :
    # 'Timestamp (Hour Ending)'
    # 'Demand (MWh)'
    def wrangle_fpl_load_curve_data(filename):
        rel_path = filename
        load_curve_data = os.path.join(script_dir, rel_path) 
        data = LoadData.get_csv(load_curve_data,['Timestamp (Hour Ending)','Demand (MWh)'])
        data_clean = LoadData.clean_data(data)
        data_clean_iso = LoadData.convert_date_time_to_ISO(data_clean)
        data_clean_iso_norm =  LoadData.convert_normalize_pwr(data_clean_iso)
        return data_clean_iso_norm    
    def get_csv(file,col_names):
        output = []
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = []
                for col in col_names:
                    r.append(row[col])
                output.append(r)
        return output
    def clean_data(data):
        #remove rows with empty field
        output = []
        skip = False
        for r in data :
            for c in r:
                if c=='':
                    skip = True
                else :
                    skip = False
            if not skip:
                output.append(r)
        return output
    def convert_date_time_to_ISO(data):
        from dateutil.parser import parse
        output = []
        for r in data :
            dt = parse(r[0])
            r[0] = dt.isoformat()
            output.append(r)
        return output
    def convert_normalize_pwr(data):
        output = []
        for r in data :
            r[1] = int(r[1])/2
            output.append(r)
        return output
    

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

    main()