# TODO

## Week 10 : 4/9/2021
[ ] Capture the gametheory into a report 
 -  Combine the material from the thesis and add the material we made for 

## Week 10 : 4/9/2021
[ ] Fuzzy logic implementation (Create this for 3,5,10)
- recreate fuzzy logic function and compare the payment to game theory payment
- compare it with 3 customers first, between shapley and fuzzy 

[ ] Develop powerpoint slides
    - What are we working on
    - What is the plan
        - Topics
            - Optimal Design of Hybrid Generation for EV's Charging Stations
            - P2P Energy Trading ... 
            - Game Theoretic Design of Payments for Coalitions vs. Fuzzy Logic Design of Payments for Coalition

[ ] Meet with dr.Abtahi (send an email and get a time scheduled)
    [ ] Schedule a meeting with committee after dr.Abtahi meeting
    [ ] Dr. Zhuang, Dr. Roth, Dr. Abtahi

[ ] Documents to be filled out by Dr.Z
[ ]  Review the paper w/ Dr.Z
[ ] hamidreza.mahini@gmail.com , see if he or matlab can help you make this shapley calculation faster for >13 , 
Couldnt find the email from the guy who wrote it in python 
-ask matlab support to see if they can help





## Week 9 : 3/29/2021
[ ] Look at three issues
 1. INcrease dataset and see how we can build a response for the coalition for large number of customers
 2. Designers will leverage the non-linear payments for coalitions, how will this be modified? What is a large shapley coalition for?
    - how many customers do we ned as a coalition to provide value to FPL?
    - choose a region and figure out how many customers we need for htis to work?
    - how much energy needs to be reserved? can i provide the reserve power through a PV coalition?
    - can we pay them on a exponential characteristic function
    - ex. 10MW of reserve required for central florida region, the customers can provide this reserve , how many prosumers would i need to supply this and how much incentive would i need to encourage this?
    - without sufficient number customers how can i increase my incentives to improve my capacity?
    - how do we include the energy storage to confirm coalition can provide energy when requested and act as a reserver

[ ] Sensitivity of 'a' ,
- it is a predetermined value, and understand it iwth respect to other parameters, 
- try to provide the sensitivity with respect to the energy consumption .
- how does it effect the function if we have a convex characteristiv function




## Week 8 : 3/25/2021
[X] use the values from the thesis, to validate the 3,5,10 customers. test it again.
- Copy data from thesis 
- input into the same process 
- test output
[X] Recreate table 4.8 for different value of X^n
    - allow n to be a continuou value
[X] Replicated the Tables for Fall/Winter/Spring of Pecan Data set
[X] Apply the EIA.gov data for similar time frames 

[ ] Sensitivity of 'a' scale analysis in Table for (tp-tc) parameters

[ ] Fuzzy logic implementation of the demand/cost curve based on prosumer generation and demand
    - prosumer generation low, consumer demand low, cost of energy high, price for energy low
    - prosumer generation high, consumer demand low, cost of energy low, price for energy low
    - prosumer generation high, consumer demand high, cost of energy low, price for energy low
    - prosumer generation low, consumer demand high, cost of energy high, price for energy high

## Week 8 : 3/15/2021

[X] update sensitivy formula , and provide an analysis with respect to G and with respect to (tp-tc)

[X] Fuzzy Example 1 : 1-input to 1-output : Just look at consumption as a membership function where the user can consume a range of energy and the output would be a particular price (lo,med,high)
 - assume that hte energy range woul dbe different levels of pricing tiers

[X] Fuzzy Example 2 : 2-input to 1-output : use matlab to derive the fuzzy logic rules, try only cost output with gen/dem 

[X] Fuzzy Example 3 : 2-input to 1-output : use matlab to derive the fuzzy logic rules, try only pricing output with gen/dem

[X] Use some test data to validate the simple cases, compare to what we are gettignw ith pricing (1-10) items 



## Week 7 : 3/8/2021
[X] Recreate table 4.8 for different value of X^n
    - allow n to be a continuou value
[X] Sensitivity of 'a' scalar worked out by hand 
[ ] Fuzzy logic implementation of the demand/cost curve based on prosumer generation and demand
    - prosumer generation low, consumer demand low, cost of energy high, price for energy low
    - prosumer generation high, consumer demand low, cost of energy low, price for energy low
    - prosumer generation high, consumer demand high, cost of energy low, price for energy low
    - prosumer generation low, consumer demand high, cost of energy high, price for energy high
[ ] Show a growth of revenue in a chart for each trial of N



## Week 6 : 3/3/2021


[X] N=5 and N=10 user to get the prosumer for shapley

[] check to see if its the same trend. if not then change the implementation method for CHarictersitc values.

[ ] Do we have to change the contribution of the users.


## Week 5 : 2/21/2021

[X] Loop, and Data fixes with 100 prosumers

[X] loop through char functions fo rN prosumers

[X] identify perfect value for a?


---

[X] Color map adjust red to green. for N-3

[ ] the generators or now generating to much , can we increase the tiers gradually. 

[X] Generate all the data you need initially

[] See how the game theory works for coalition 

[] understand how the 'a' scale should change?

[ ] What is the difference between profit with coalition an profit without coalition?

[X] Setup 100 prosumers as Shapley coalition and analysis payment

[ ] keep 'a' fixed 

[X] Can you generate data and increase the production size for each home by 50%,100%, 120% generation and graph (n=3,5,100)

[ ] Contradict the assumption presented by Vottem theses
    - if we exceed the production by twice the consumption, 'g' would not pay out any more, i.e. it has been maximized.

## Week 4 : 2/15/2021

[X] Hide the line number on the output table. , and put hte ID number in the first column. 

[X] Create better illustrations of the graphs, by combining the graphs for each prosumer
- use an average
- create a more undertandable graph
- try creating a 3d graph of the multiple dimensions
- what is teh story you want to show here for each prosumer?
- xyz, time , 
- total profit, average profit?
- combine all and consider totla profit of all prosumers as one aspect 
- try showing quarterly result as a bargraph

[X] Build a n=3 , 5 or 100 condition for the shapley, ie. make it recursive algo for characterisitcs



---
## Week 3 : 2/5/2021

[X] Setup 3 prosumers as Shapley coalition
    - Shapley payoff with NRG

[X] split prosumers into a coalition

[X] Validate the h function with prosumer curves

---
## Week 2 : 1/29/2021

[X] add excerpt of data for florida from NREL
Average Ranges for Direct Normal Solar Irradiance for the State of Florida
jan:4.5-5.4
feb:5.4-5.9
mar:5.5-6.4
apr:6.0-6.9
may:6.0-7.0
jun:5.0-5.9
jul:4.0-5.4
aug:<4.0-4.9
sep:<4.0-4.4
oct:5.0-5.9
nov:5.0-5.9
dec:<4.0-4.9

[X] Add the 100 customers to simulation 

[X] Add the consumption 

[X] Update nrg exchange to include consumption of energy h(.) 


---
## Week 1 : 1/22/2021

[X] Validate the dataset

[X] Use 12 months 

~[ ] Multiple years, analysis?~

~[ ] Remove restriction for the generation how much better can i have?~

[X] Fix graphs with details

~[ ] Setup 100 prosumers as Shapley coalition and analysis payment~

[X] Redesign to include energy consumed

~[ ] Update nrg exchange to include consumption of energy h(.)~ 

[X] Seperate net metering analysis on a different file 

