import pandas as pd
import model as m
import numpy as np

# Step 4 : Design model inside of an experiment
def run_sim(prosumers,args):
    # Distribution Service Operator manages payback for each substation
    dso = m.DSO(args=args)
    for substation in dso.substations:
        substation.connect(prosumers)
    dso.run()
    print("Step 4: Simulation completed.")
    return dso

def test(prosumers,args):
    dso = run_sim(prosumers,args)
    for substation in dso.substations:
        print(f"{substation.id} : items={len(substation.prosumers)}")
        for p in substation.prosumers:
            print(f"prosumer:{p.id},balance={p.get_balance()},prod={p.get_prod_total()},con={p.get_con_total()}")   
    return dso

def optimize():
    import scipy.optimize as optimize
    initial_guess = [1, 1, 1]
    result = optimize.minimize(f, initial_guess)
    if result.success:
        fitted_params = result.x
        print(fitted_params)
    else:
        raise ValueError(result.message)
def f(params):
    # print(params)  # <-- you'll see that params is a NumPy array
    a, b, c = params # <-- for readability you may wish to assign names to the component variables
    return a**2 + b**2 + c**2

