import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import model
import datetime


def sim_performance(dso,T):    
    #Profit Curves
    title = "Payout Curves"



    for fig_i in range(len(dso.substations)):
        plt.figure(fig_i)                # the first figure  :
        plt.subplot(231)
        plt.ylabel = "kWh"
        plt.title("Production")
        for p in dso.substations[fig_i].prosumers:
            plt.plot(p.get_production_curve(T),label=f"Prosumer {p.id}")
        #plt.legend()

        plt.subplot(232)
        plt.ylabel = "kWh" 
        plt.title("Consumption")           
        for p in dso.substations[fig_i].prosumers:
            plt.plot(p.get_consumption_curve(T),label=f"Prosumer {p.id}")
        #plt.legend()

        plt.subplot(233)
        plt.ylabel = "kWh"
        plt.title("Net Energy")
        for p in dso.substations[fig_i].prosumers:
            plt.plot(p.get_input_energy_curve(T),label=f"Prosumer {p.id}")
        #plt.legend() 

        plt.subplot(234)
        plt.ylabel = "$/kWh"
        plt.title("Payments")
        for p in dso.substations[fig_i].prosumers:
            plt.plot(p.get_payments_curve(T),label=f"Prosumer {p.id}")
        #plt.legend()

        plt.subplot(235)
        plt.ylabel = "Total $/kWh"
        plt.title("Total Balance")           
        for p in dso.substations[fig_i].prosumers:
            plt.plot(p.get_total_balance_curve(T),label=f"Prosumer {p.id}")
        #plt.legend()

        plt.subplot(236)
        plt.ylabel = "kWh"
        plt.title("tp>>tc")           
        for p in dso.substations[fig_i].prosumers:
            con = p.get_consumption_curve(T)
            prod = p.get_production_curve(T)
            x=[]  
            for i in range(T):
                if (prod[i] > 2 * con[i]):
                    x.append(prod[i])
                else:
                    x.append(0)
            plt.plot(x,label=f"Prosumer {p.id}")
        #plt.legend()

        plt.show()
