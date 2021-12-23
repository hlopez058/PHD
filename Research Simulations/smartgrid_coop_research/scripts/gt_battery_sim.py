from itertools import combinations
import math
import bisect
import sys

def batterylife_characteristic_function(n,args=None):
    '''
    Characteristic equation that calculates the 
    combined contribution of a group. If it is a 
    linear sum then the result of n[1] and n[2]
    should be n[1] + n[2]. Note: a linear combination
    will result in equal distribution of payout

    Use the 'args' object to refrence any constants
    or coefficients used in the characteric equation 
    '''
    result = 0
    for i in n:
        result += i

    # distribute the demand evenly across n players
    # calculate the deterioration for each divided demand
    # for all players in n in group 
    return result

def main():
    
    battery_states = {
      "1":10,
      "2":11
    }

    demand = 10

    battery_damage = [10,12]
    
    print(battery_damage)
    
    shp = ShapleyClass(
        players_contributions = battery_damage,
        characteristic_func =  batterylife_characteristic_function,
        args= {})
    
    print(f"{shp.shapley}")



class ShapleyClass():
    # Constructor 
    def __init__(self,players_contributions,characteristic_func,args): 
        self.n =players_contributions
        self.v = self.get_characteristic_values(characteristic_func,args)
        self.shapley = self.get_shapley(self.n,self.v)
        self.shapley_wo_coalition= self.get_shapley_wo_coalition(characteristic_func,args)
        self.shapley_avg = self.average(self.get_shapley(self.n,self.v))

    def power_set(self,List):
        PS = [list(j) for i in range(len(List)) for j in combinations(List, i+1)]
        return PS
    def average(self,List):
        return sum(List) / len(List)
    def get_shapley(self,n,v): 
        tempList = list([i for i in range(len(self.n))])
        N = self.power_set(tempList)
        shapley_values = []
        for i in range(len(self.n)):
            shapley = 0
            for j in N:
                if i not in j:
                    cmod = len(j)
                    Cui = j[:]
                    bisect.insort_left(Cui,i)
                    l = N.index(j)
                    k = N.index(Cui)
                    var_temp = float(v[k]) - float(v[l]) 
                    num_temp = float( var_temp * float(math.factorial(cmod)\
                         * math.factorial(len(self.n) - cmod - 1)))
                    dem_temp = float(math.factorial(len(self.n)))
                    temp = num_temp/dem_temp
                    shapley += temp
            cmod = 0
            Cui = [i]
            k = N.index(Cui)
            temp = float(v[k]) * float(math.factorial(cmod) * \
                math.factorial(len(self.n) - cmod - 1)) / float(math.factorial(len(self.n)))
            shapley += temp
            shapley_values.append(shapley)
        return shapley_values
    def get_characteristic_values(self,func,args):
        all_coalitions = []
        for size in range(1,len(self.n)+1) :
            combos = list(combinations(self.n,size))
            coalitions = []
            for combo in combos:
                val = func(combo,args)
                coalitions.append(val)
            for x in coalitions:
                all_coalitions.append(x)
        return all_coalitions
    def get_shapley_wo_coalition(self,func,args):
        num_of_players = len(self.n)
        psi_wo_coalition  = [func([num_of_players],args) for num_of_players in self.n]
        return psi_wo_coalition

if __name__ == '__main__':
    main()
