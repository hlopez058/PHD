import pandas as pd
import os
import random
import math
import random
from numpy import random

class DSO():
    def __init__(self,args):
        """
        Distribute System operator
        Manages a series of substations
        num_of_stations: is the number of substations elements
        q : max rate of return ($/kWh)
        a : scaling factor for payout characteristic function 'g'
        n : exponential rates for input energy
        """
        self.q = args['g']['q']
        self.a = args['g']['a']
        self.n = args['g']['n']
        self.T = args['T']
        self.substations = []
        for i in range(args['K']):
            self.substations.append(Substation(id=i))
    
    def run(self):
        """
        T : maxium window size to run simulation of payout
        """
        for t in range(self.T):
            self.payout(t)

    def payout(self,t):
        for substation in self.substations:
            tc = substation.get_tc(t)
            tp = substation.get_tp(t)
            for prosumer in substation.prosumers:
                x = prosumer.input_energy(t)
                payment = self.g(x=x,tp=tp,tc=tc,n=self.n,q=self.q,a=self.a)
                prosumer.get_paid(t=t,payment=payment)

    def g(self,x,tp,tc,n,q,a):
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
        try:
            ans = float(math.pow(x,n)*q/math.exp(math.pow(tp-tc,2)/a))
        except OverflowError:
            ans = float('inf')
        return ans

    def h(self,y,tp,tc,n,r):
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

class Substation():
    def __init__(self,id):
        """
        Electrical substation collects input energy
        calculates the total production and total 
        consumption of the connected prosumers
        """
        self.id = id
    def connect(self,prosumers):
        self.prosumers = prosumers
    def get_tc(self,t):
        tc = sum([ p.consumption(t) for p in self.prosumers])
        return tc
    def get_tp(self,t):
        tp = sum([ p.production(t) for p in self.prosumers])
        return tp
 


class Prosumer():
    def __init__(self,id,args,gen_curve,dem_curve):
        """
        A home that can consume and
        produce energy from a local power 'Plant'
        with some capacity limit
        """
        self.id = id
        self.gen_curve = gen_curve
        self.dem_curve = dem_curve
        self.demand_mean = args['demand']['mean']
        self.demand_std = args['demand']['std']
        self.capacity_std = args['demand']['std']
        self.capacity_mean = args['capacity']['mean']
        self.ledger = [{"t":0,"payment":0,"balance":0}]
        self.gen_act_curve = []
        self.dem_act_curve = []

    def get_paid(self,t,payment):
        prev_balance = self.ledger[-1]['balance']
        if payment == float('inf'):
            payment = 0
        self.ledger.append({"t":t,"payment":payment,"balance": prev_balance + payment})
    def get_balance(self):
        return self.ledger[-1]['balance']
    def get_prod_total(self):
        return sum(self.gen_act_curve)
    def get_con_total(self):
        return sum(self.dem_act_curve)
        
    def input_energy(self,t):
        """
        input energy, 'x' is the 
        net energy of the prosumer
        considering consumption and production
        """
        return max(0,self.production(t) - self.consumption(t))
    def production(self,t):
        """
        Return production in kWh at some time 't'
        the generation curve is normalized so it
        is multiplied by the capacity and some
        random effeciency noise (80 to 100%)
        """
        x = random.normal(loc=self.capacity_mean,scale=self.capacity_std,size=None)
        #effeciency = random.randint(80,100) * 0.01
        val =  self.gen_curve[t] * x 
        self.gen_act_curve.append(val)
        return val
    def consumption(self,t):
        """
        Return consumption of prosumer home based on
        residential consumption model
        """
        #effeciency = random.randint(100,100) * 0.01
        x = random.normal(loc=self.demand_mean,scale=self.demand_std,size=None)
        val = self.dem_curve[t] * x
        self.dem_act_curve.append(val)
        return val
    def _get_curve(self,func,T):
        try:
            if T == None :
                T = min(len(self.gen_curve),len(self.dem_curve))
            else:
                #print(f"T = {T} ; ledger_lenn = {len(self.ledger)}")
                return [func(t) for t in range(T)]
        except:
            print("An exception occurred")
    def get_production_curve(self,T=None):
        return self._get_curve(self.production,T)
    def get_consumption_curve(self,T=None):        
        return self._get_curve(self.consumption,T)
    def get_input_energy_curve(self,T=None):
        return self._get_curve(self.input_energy,T)
    def get_payments_curve(self,T=None):
        #print(len(self.ledger))
        return self._get_curve(lambda x: self.ledger[x]['payment'] ,T)
    def get_total_balance_curve(self,T=None):
        return self._get_curve(lambda x: self.ledger[x]['balance'] ,T)

