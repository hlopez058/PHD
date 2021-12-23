from itertools import combinations
import math
import bisect
import sys

def power_set(List):
    PS = [list(j) for i in range(len(List)) for j in combinations(List, i+1)]
    return PS

def get_shapley(n,v): 
    tempList = list([i for i in range(n)])
    N = power_set(tempList)
    shapley_values = []
    for i in range(n):
        shapley = 0
        for j in N:
            if i not in j:
                cmod = len(j)
                Cui = j[:]
                bisect.insort_left(Cui,i)
                l = N.index(j)
                k = N.index(Cui)
                var_temp = float(v[k]) - float(v[l]) 
                num_temp = float( var_temp * float(math.factorial(cmod) * math.factorial(n - cmod - 1)))
                dem_temp = float(math.factorial(n))
                temp = num_temp/dem_temp
                shapley += temp
        cmod = 0
        Cui = [i]
        k = N.index(Cui)
        temp = float(v[k]) * float(math.factorial(cmod) * math.factorial(n - cmod - 1)) / float(math.factorial(n))
        shapley += temp
        shapley_values.append(shapley)
    return shapley_values

def get_characteristic_values(n,func,args):
    all_coalitions = []
    for size in range(1,len(n)+1) :
        combos = list(combinations(n,size))
        coalitions = []
        for combo in combos:
            val = func(combo,args)
            coalitions.append(val)
        #for x in unique(coalitions):
        for x in coalitions:
            all_coalitions.append(x)
    #print(all_coalitions)
    return all_coalitions
# Characteristic function 
# input is an array of inputs for each player
def characteristic_function(n,args=None):
    result = 0
    for i in n:
        result += i 
    return pow(result,2) * 0.12 
    #return math.sqrt(result)* 0.12 

def nrg_char_func(n,args):
    X = 0
    for i in n:
        X += i 
    q=0.1
    a=1000
    tx = args['tx'] # tp - tc
    try:
        ans = float(X*q/math.exp(math.pow(tx,2)/a))
    except OverflowError:
        ans = float('inf')
    return ans
    #return pow(result,2) * 0.12 
    #return math.sqrt(result)* 0.12 

def nrg_pecan_char_func(n,args):
    X = 0
    for i in n:
        X += i 
    q=10
    a=math.pow(10,6)
    tx = args['tx'] # tp - tc
    try:
        ans = float(X*q/math.exp(math.pow(tx,2)/a))
    except OverflowError:
        ans = float('inf')
    return ans
    #return pow(result,2) * 0.12 
    #return math.sqrt(result)* 0.12 

def nrg_pecan_exp_char_func(n,args):
    X = 0
    for i in n:
        X += i 
    q=10
    a=math.pow(10,6)
    tx = args['tx'] # tp - tc
    nu = args['nu'] # X^n
    try:
        ans = float(math.pow(X,nu)*q/math.exp(math.pow(tx,2)/a))
    except OverflowError:
        ans = float('inf')
    return ans
    #return pow(result,2) * 0.12 
    #return math.sqrt(result)* 0.12 

def average(list):
    return sum(list) / len(list)

def get_shapley_average(n,v):
    return average(get_shapley(n,v))

def get_shapley_wo_coalition(players_contributions,func,args):
    n = len(players_contributions)
    psi_wo_coalition  = [func([n],args) for n in players_contributions]
    return psi_wo_coalition


def get_table_4_8():
    all_players = [100,30,85,70,60,45,20,15,90,110]
    for N in range(2,len(all_players)+1):
        players_contributions = all_players[:N]
        #print(players_contributions)
        n = len(players_contributions)
        v = get_characteristic_values(players_contributions,characteristic_function,None)
        average_shapley = average(get_shapley(n,v))
        average_shapley_wo_co  = average(get_shapley_wo_coalition(players_contributions))
        print(f"{N},{average_shapley},{average_shapley_wo_co}")


def get_table_5_5():
    set_all_players = [
        [50,-30,60,-60,-35],
        [50,-20,60,-60,-35],
        [50,0,60,-60,-35],
        [50,30,60,-60,-35],
        [50,70,60,-60,-35]
    ]

    for all_players in set_all_players:
        players_contributions = all_players
        #print(players_contributions)
        n = len(players_contributions)
        v = get_characteristic_values(players_contributions,nrg_char_func,args={
            "tx":sum(all_players)
        })
        g = get_shapley(n,v)
        average_shapley = average(g)
        print(f"{n},{average_shapley},{g}")



def get_table_5_6():
    set_all_players = [
        [-30,-10,-31,-25,-15],
        [-20,0,-21,-15,-5],
        [0,20,-1,5,15],
        [30,50,29,35,45],
        [70,90,69,75,85]
    ]

    for all_players in set_all_players:
        players_contributions = all_players
        #print(players_contributions)
        n = len(players_contributions)
        v = get_characteristic_values(players_contributions,nrg_char_func,args={
            "tx":sum(all_players)
        })
        g = get_shapley(n,v)
        average_shapley = average(g)
        print(f"{n},{average_shapley},{g}")

def get_pecan_tables():
    set_all_players = [
        [-50,159,639,-327,1061,420],
        [83,658,959,-184,1247,214],
        [101,142,583,-235,1041,597]
    ]

    for all_players in set_all_players:
        players_contributions = all_players
        #print(players_contributions)
        n = len(players_contributions)
        v = get_characteristic_values(players_contributions,nrg_pecan_char_func,args={
            "tx":sum(all_players)
        })
        g = get_shapley(n,v)
        go = get_shapley_wo_coalition(players_contributions,nrg_pecan_char_func,args={
            "tx":sum(all_players)
        })
        average_shapley = average(g)
        print(f"{g}")
        #print(f"{go}")

def get_pecan2_tables():
    set_all_players = [
    [159,420,639,1061],
    [658,214,959,1247],
    [142,597,583,1041]
    ]

    for all_players in set_all_players:
        players_contributions = all_players
        #print(players_contributions)
        n = len(players_contributions)
        v = get_characteristic_values(players_contributions,nrg_pecan_exp_char_func,args={
            "tx":sum(all_players),
            "nu":2
        })
        g = get_shapley(n,v)
        go = get_shapley_wo_coalition(players_contributions,nrg_pecan_exp_char_func,args={
            "tx":sum(all_players),
            "nu":2
        })
        average_shapley = average(g)
        print(f"{g}")
        #print(f"{go}")


#get_pecan2_tables()

get_table_4_8()

results_data = {
    "x_2" : {
        "w_coalition" : [1014,1849,2436.75,2856.6,3042,2881.7,2709.3,3536.3,3000],
        "wo_coalition" : [654,725,690.75,639,573,498,438.7,498.3,300]
    } ,
    "x_1":{
        "w_coalition" : [7.8,8.6,8.55,8.28,7.8,7.025,6.375,6.866,6],
        "wo_coalition" : [7.8,8.6,8.55,8.28,7.8,7.025,6.375,6.866,6]
    },
    "x_0.5":{
        "w_coalition" : [0.6838,0.5865,0.5064,0.4458,0.3949,0.3471,0.3092,0.3025,0.2683],
        "wo_coalition" : [0.9286,0.9878,0.9919,0.9794,0.9503,8.912,0.8379,0.8713,0.8485]
    }
}



