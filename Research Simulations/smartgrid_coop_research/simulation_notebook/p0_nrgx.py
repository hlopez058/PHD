import bisect
from itertools import combinations
from IPython.display import display, HTML
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool, Value
from datetime import datetime
import math
from datetime import timezone

# NRGXChange Payment g(.) Function


def g(price, X, tp, tc, a, n):
    q = price
    try:
        pay = (pow(X, n)*q)/math.exp(pow((tp-tc), 2)/a)
    except OverflowError:
        pay = float('inf')
    return pay

# NRGXChange Charge h(.) Function


def h(price, Y, tp, tc):
    r = (0.01*price)
    try:
        cost = (Y*r*tc)/(tc+tp)
    except OverflowError:
        cost = float('inf')
    return cost


# Shapley Value Python Logic
# Authored by Susobhan Ghosh
# https://github.com/susobhang70
# Committed on 02/01/2020
# Create Combinatorial from List


def power_set(List):
    PS = [list(j) for i in range(len(List)) for j in combinations(List, i+1)]
    return PS
# Calculate Shapley from Characteristic Value list


def get_shapley(n, v):
    tempList = list([i for i in range(n)])
    N = power_set(tempList)
    shapley_values = []
    for i in range(n):
        shapley = 0
        for j in N:
            if i not in j:
                cmod = len(j)
                Cui = j[:]
                bisect.insort_left(Cui, i)
                l = N.index(j)
                k = N.index(Cui)
                temp = float(float(v[k]) - float(v[l])) *\
                    float(math.factorial(cmod) * math.factorial(n -
                          cmod - 1)) / float(math.factorial(n))
                shapley += temp
        cmod = 0
        Cui = [i]
        k = N.index(Cui)
        temp = float(v[k]) * float(math.factorial(cmod) *
                                   math.factorial(n - cmod - 1)) / float(math.factorial(n))
        shapley += temp
        shapley_values.append(shapley)
    return shapley_values


def test_shapley():
    # Test of Shapley Function Calculation
    # Results in Shapley distribution of : Prosumer-1: $0.65, Prosumer-2: $0.39
    n = 2
    p1_characteristic_value = 0.77
    p2_characteristic_value = 0.51
    p1_n_p2_characteristic_value = 1.04
    v = [p1_characteristic_value, p2_characteristic_value,
         p1_n_p2_characteristic_value]
    vals = get_shapley(n, v)
    print(f"Prosumer-1: ${vals[0]}, Prosumer-2: ${vals[1]}")


####################################################################
# Calculate the shapley value given the net energy and the average
# generation and consumption values
####################################################################
t_async = None  # global for multiprocessing of df time slices


def get_nrg_payments(df, price, n, a, drop_negative_contribution=False):
    i = 0
    for t in df:
        #print(f"processing t={i} of {len(df)}")
        i = i+1
        # drop the prosumer from consideration if the energy offered
        # by the prosumer is a negative value
        if drop_negative_contribution:
            index_names = t[t['net_energy'] < 0].index
            t.drop(index_names, inplace=True)

        tp = t['generation'].sum()
        tc = t['consumption'].sum()
        net_energy = t['net_energy']

        # shapley without coalition, only depends on characteristic
        # equation Y=X^n
        t['shapley_wo_coalition'] = net_energy.apply(lambda x:
                                                     g(price=price, X=x, tc=tc, tp=tp, n=n, a=a))

        # Implement shapley function
        # Use the id of each prosumer in order to build a factorial powerset
        # the power set is used by summing the energy contributed as a coalition
        # the aggregate energy is then sent to NRG payment function
        # the response is the shapley contribution payout for that coalition
        List = t['id'].values.tolist()
        List.sort()
        #print(f"Generationg power set")
        # print(List)

        start_time = datetime.now()
        PS = get_power_set(List)
        end_time = datetime.now()
        #print('Power Set Combination: {}'.format(end_time - start_time))

        shapley_contributions = []
        global t_async
        t_async = t
        start_time = datetime.now()
        with Pool(10) as p:
            shapley_contributions.extend(
                (p.imap(get_shapley_contribution, PS, 100)))
        end_time = datetime.now()
        #print('Calculating Marginal Contributions: {}'.format(end_time - start_time))

        shapley_values = []
        start_time = datetime.now()
        for contribution in shapley_contributions:
            shapley_values.append(get_shapley_value(
                contribution, price, tc, tp, a, n))
        end_time = datetime.now()
        #print('Calculating Shapley Values : {}'.format(end_time - start_time))

        start_time = datetime.now()
        t['shapley_w_coalition'] = get_shapley(len(t['id']), shapley_values)
        end_time = datetime.now()
        #print('Calculating Grand Coalitions Shapley Values : {}'.format(end_time - start_time))

    return df


def get_net_payments(df, price, n, a, drop_negative_contribution=False):
    i = 0
    for t in df:
        #print(f"processing t={i} of {len(df)}")
        i = i+1
        net_energy = t['net_energy']
        t['net_metering'] = price*net_energy
    return df


def get_shapley_value(contribution, price, tc, tp, a, n):
    # get nrg payment for the contribution of the coalitional combination
    nrg_payment = g(price=price, X=contribution, tc=tc, tp=tp, n=n, a=a)
    return nrg_payment


def get_shapley_contribution(coalition_combination):
    global t_async
    t = t_async
    # energy contribution of the coalitional combination
    contribution = t.loc[t['id'].isin(
        coalition_combination)]['net_energy'].sum()
    return contribution


def get_power_set(List):
    PS = [list(j) for i in range(len(List)) for j in combinations(List, i+1)]
    return PS


def apply_payments(trial, a, n):
    N = trial['N']
    df_by_t = trial['df_by_t']
    price = trial['df']['price'].max()
    trial['df_by_t'] = get_nrg_payments(
        df_by_t, price=price, a=a, n=n, drop_negative_contribution=True)
    return trial


def apply_net_meter_payments(trial, a, n):
    N = trial['N']
    df_by_t = trial['df_by_t']
    # https://www.fpl.com/content/dam/fpl/us/en/rates/pdf/Residential%20(Effective%20January%202021).pdf
    price = 0.1098
    trial['df_by_t'] = get_net_payments(
        df_by_t, price=price, a=a, n=n, drop_negative_contribution=True)
    return trial


def trials_apply_payments(trials, a, n):
    for trial in trials:
        N = trial['N']
        df = trial['df']
        df_by_t = trial['df_by_t']
        price = df['price'].max()
        trial['df_by_t'] = get_nrg_payments(
            df_by_t, price=price, a=a, n=n, drop_negative_contribution=True)
    return trials


def plot_trials_old(trials, n):
    for trial in trials:
        X = [x for x in trial['df']['time'].unique().tolist()]
        Y_wo = [t['shapley_wo_coalition'].sum() for t in trial['df_by_t']]
        Y_w = [t['shapley_w_coalition'].sum() for t in trial['df_by_t']]
        Z = [t['net_energy'].sum() for t in trial['df_by_t']]
        ax = plt.axes(projection='3d')
        ax.set_title(f"EIA.gov Trial-N={trial['N']},X^{n}", loc="right")
        ax.set_xlabel("Time")
        ax.set_ylabel("Shapley Value")
        ax.set_zlabel("Net Energy")
        ax.scatter3D(X, Y_wo, Z, c=Z, cmap='Blues')
        ax.plot3D(X, Y_wo, Z, 'blue', label='Without Coalition', marker='o')
        ax.scatter3D(X, Y_w, Z, c=Z, cmap='Reds')
        ax.plot3D(X, Y_w, Z, 'red', label='With Coalition', marker='x')
        ax.legend(loc='upper left')
        plt.show()
        # print_tables(df_by_t,n=1.5)


def plot_net_trials(trials, n):
    import matplotlib.dates as md
    for trial in trials:
        X = [t['time'].iloc[0] for t in trial['df_by_t']]
        Y_wo = [t['shapley_wo_coalition'].sum() for t in trial['df_by_t']]
        Y_w = [t['net_metering'].sum() for t in trial['df_by_t']]
        Z = [t['net_energy'].sum() for t in trial['df_by_t']]
        ax = plt.gca()
        xfmt = md.DateFormatter('%Y-%m')
        plt.xticks(rotation=90)
        ax.xaxis.set_major_formatter(xfmt)
        #ax = plt.axes(projection='3d')
        ax.set_title(f"EIA.gov Trial-N={trial['N']},X^{n}", loc="right")
        ax.set_xlabel("Time")
        ax.set_ylabel("Profit (cents/$)")
        #ax.set_zlabel("Net Energy")
        #ax.scatter3D(X, Y_wo, Z, c=Z,cmap='Blues');
        #ax.plot3D(X, Y_wo, Z,'blue',label='NRG-X-Change',marker='o');
        #ax.scatter3D(X, Y_w, Z, c=Z,cmap='Reds');
        #ax.plot3D(X, Y_w, Z,'red',label='Net-Metering',marker='x');
        ax.plot(X, Y_wo, label='NRG-X-Change', marker='o', color='b')
        ax.plot(X, Y_w, label='Net-Metering', marker='x', color='r')
        ax.legend(loc='upper left')
        plt.show()
        # print_tables(df_by_t,n=1.5)


def plot_trials(trials, n):
    for trial in trials:
        X = [t['time'].iloc[0].replace(
            tzinfo=timezone.utc).timestamp() for t in trial['df_by_t']]
        Y_wo = [t['shapley_wo_coalition'].sum() for t in trial['df_by_t']]
        Y_w = [t['shapley_w_coalition'].sum() for t in trial['df_by_t']]
        Z = [t['net_energy'].sum() for t in trial['df_by_t']]
        ax = plt.axes(projection='3d')
        ax.set_title(f"EIA.gov Trial-N={trial['N']},X^{n}", loc="right")
        ax.set_xlabel("Time")
        ax.set_ylabel("Shapley Value")
        ax.set_zlabel("Net Energy")
        ax.scatter3D(X, Y_wo, Z, c=Z, cmap='Blues')
        ax.plot3D(X, Y_wo, Z, 'blue', label='Without Coalition', marker='o')
        ax.scatter3D(X, Y_w, Z, c=Z, cmap='Reds')
        ax.plot3D(X, Y_w, Z, 'red', label='With Coalition', marker='x')
        ax.legend(loc='upper left')
        plt.show()
        # print_tables(df_by_t,n=1.5)


def plot_bar_trials(trials, n):
    for trial in trials:
        X = [t['time'].iloc[0].replace(
            tzinfo=timezone.utc).timestamp() for t in trial['df_by_t']]
        Y_wo = [t['shapley_wo_coalition'].sum() for t in trial['df_by_t']]
        Y_w = [t['shapley_w_coalition'].sum() for t in trial['df_by_t']]
        Z = [t['net_energy'].sum() for t in trial['df_by_t']]
        ax = plt.axes(projection='3d')
        ax.set_title(f"EIA.gov Trial-N={trial['N']},X^{n}", loc="right")
        ax.set_xlabel("Time")
        ax.set_ylabel("Shapley Value")
        ax.set_zlabel("Net Energy")
        ax.scatter3D(X, Y_wo, Z, c=Z, cmap='Blues')
        ax.plot3D(X, Y_wo, Z, 'blue', label='Without Coalition', marker='o')
        ax.scatter3D(X, Y_w, Z, c=Z, cmap='Reds')
        ax.plot3D(X, Y_w, Z, 'red', label='With Coalition', marker='x')
        ax.legend(loc='upper left')
        plt.show()

        # create a dataset
        height = [3, 12, 5, 18, 45]
        bars = ('A', 'B', 'C', 'D', 'E')
        x_pos = np.arange(len(bars))

        # Create bars with different colors
        plt.bar(X, height, color=['black', 'red', 'green', 'blue', 'cyan'])

        # Show graph
        plt.show()

        # print_tables(df_by_t,n=1.5)
