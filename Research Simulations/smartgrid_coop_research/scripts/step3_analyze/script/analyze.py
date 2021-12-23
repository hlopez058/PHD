# Derived from Application of cooperative game theory in smart grids
# Thesis reference by Vottem University of texas
# Simualtion of system model 4.1.1
import math
import random
import os
import csv

def main():
    for env in environments:
        substation = Substation(id=1,num_of_prosumers=3)

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
    def get_tc(self,t):
        tc = sum([ p.Consumption(t) for p in self.Prosumers])
        return tc
    def get_tp(self,t):
        tp = sum([ p.Production(t) for p in self.Prosumers])
        return tp

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
    def Production(self,env, t):
        """
        Return production in kWh at some time 't'
        """
        return env[t]['']
    def Consumption(self,t):
        """
        Return consumption of prosumer home based on
        residential consumption model
        """
        average_load = 877/730 # 877 kWh per month
        return average_load

class Plant():
    def __init__(self,capacity):
        """
        A plant generates energy and 
        provides it as an output energy
        for a prosumer
        """
        self.capacity = capacity
    def set_environment(self,env,t):
        self.env = env
    def output(self, t):
        """
        Output of the plant at time 't'
        """
        return random.randint(0,Solar_Irradiance[t]*self.capacity)

if __name__ == "__main__":
    from pathlib import Path
    d = Path(__file__).resolve()
    dir_root = str(d.parent.parent.parent)
    # ./script/
    dir_script =str(d.parent)
    # ./data/
    print(str(d.parent.parent))
    dir_data = os.path.join(str(d.parent.parent),'data')
    # step1_input/data
    dir_parse_data = os.path.join(dir_root,'step2_parse/data')
    parse_files = [p for p in pathlib.Path(dir_parse_data).iterdir() if p.is_file()]
    environments = [get_environment_data(f) for f in parse_files]
    main()