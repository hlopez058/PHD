# A review of Game Theory in use of Consensus Networks

Hector Lopez
Electrical, Engineering, Florida Atlantic University,
hlopez5@fau.edu

## Introduction

An electrical vehicle (EV) charging system is devised in [1] so that each charging station allows the vehicles to charge in a decentralized way. A typical charging station would require a centralized controller. The centralized controller would coordinate the charge rates of each EV with the power able to be provided by the charging system. In [1] a charging system that is powered by a solare photo-voltaic array with maximum power point tracking (MPPT), see [2], is considered along side a battery energy storage system (BESS). These two renewable energy technologies provide a way for the charging station to provide a power output at a given time that would charge the connected EV's. If the irradiance for the solar panels or the state of charge (SOC) of the battery is too low then the system would switch to a grid connected power to transfer to the EV's.

In a typical EV charging system the controller would consider the EV's connected and request the SOC of each EV and coordinate across the EV's a charge rate. The charging rate will be such that it will match the power delivered by the charging systems energy source. Since EV's could have different communication protocols, and proprietary information about the batteries performance a distributed method could be used. Each EV can calculate the optimum charge rate they need to obtain by knowing the number of other EV's connected and the total power provided by the system at a given time.

## System Configuration

In an electrical system the energy is transferred over a conductor such as a direct current (DC) bus line. A DC bus is desried since energy coming from the PV and BESS is not alternating current energy sources. The advantages of having a DC bus is to avoid the losses of energy conversion to AC , the disadvantages are the need to step up the voltage level in order to move energy effeciently large distances.

The energy captured from the sun needs to be immediately used. So when there are no connected EV's the energy is stored into the BESS. Once the SOC is high enough the PV system would sink the energy to ground or into a connection to the Grid (Allowing for net metering benefits, or offsets of other auxiliary loads). In [1] the EV's connect to charging poles on the same DC bus, but independently decipher the correct charging rate by optimizing the utility function that they all need to charge.

## Charging Method

A non-cooperative stackelberg game is used in [1] to solve the charging power distribution problem among selfish and individual players. The charging system is modeled as a lead player and the EV's are modeled as follower players. The objectives of the game are set differently for the leader and the followers. The objective of the leader is to maintain the capacity of power. That means that between the PV , BESS and the Grid, the total power available will meet the demand of the EV's. The EV's would have chargers that work with the EV's BESS to optimize the the charging needs of the EV. Such as improving the battery cycle life [4] or reducing the cost of charging [5]. In [1] the objective function to increase its charging power , ie. increase the speed of charge, is chosen. Upper and lower bounds are given based on the limits of the charging station. The logic for each player in the stakelberg game is to anticipate the output (or in this case the power consumption) of other players knowing the best response given thier optimization scheme. A series of steps in the form of backward induction allows the player to then calculate its most optimum response given the other's best responses. This would result in an equilibrium state where all players maximize the profit (revenue minus cost) of thier actions.

When working with a constrained optimization problem like the one mentioned before, the EV's only need to know the lagragian multiplier in order to deermine its charging power.

The idea is that there is a function u_i that needs to be optimized by placing a constrain on it with another function G. In [1] the constrain is the decsion of all the other's EV's to charge minus the total is less than 0. In other words that all of the EV's must be constrained to make power consumption decisions that are less than the total power available to the EV's from the charging station. This constrain is then uoverlayed on the function u_i which is the objective function of the EV making the calcualtions. The EV is trying to optimize the other players limitations from the stackelberg game against their own objective function to be able to charge. When the gradient vectors from both of these solution surfaces align, the vectors that are parallel to each other are solutions showing the constrained intersecting points between the two functions. Those points are then considered to be the maximums, or minimums.

In [6] the Karush-Kuhn-Tucker conditions of optimality ar shown to be sufficient conditions to validate the existence of the generalized nash equilibrium. That means that the KKT can be used as a serious of tests to validate that the proposed stakelberg function will acheive a stable state in which no participant can gain by a unilateral change of strategy if the strategies of the others remain unchanged [7]. The conditions identify that equilibrium is possible but the optimization of the function yields several lagrangian multipliers. By induction all of the lagragian multipliers should be the same for all of the EV's when all of the optimization functions are the same. So the langragian multiplier that is set to 0  mans that the sum of all EV power request is larger than the the total power. And when the lagragian multiplier is not 0 then the powers of each EV can be calaculated using a formula that is common for each EV and depends on the lagragian multiplier.Finally , the lagragian multiplier is what is needed to to share amongst each EV. Each EV will take the lagragian and run it its optimization during a consensus phase each EV will update teh shared lagragian value until the difference betwwen the sum ofall the EV power requets are less thant he total power provided. The recalcualtion will occur over and over to stabalize demand as EV's embark and disembark the charging stations.

## Example Simulations

## References

[1] Jing Zhang ,Consensus Network Based Distributed EnergyManagement for PV-Based Charging Station

[2]  M A Hannana, Z A Ghania, A Mohameda and M. N. Uddin, Real-Time Testing of a Fuzzy Logic Controller Based  Grid-Connected Photovoltaic Inverter System , Department of Electrical, Electronic & Systems Engineering Universiti Kebangsaan Malaysia, 43600 Bangi, Selangor, Malaysia cDepartment of Electrical Engineering, Lakehead University Thunder Bay, Ontario P7B 5E1, Canada hannan@eng.ukm.my

[3] Pablo García-Triviño,Decentralized Fuzzy Logic Control of Microgridfor Electric Vehicle Charging StationPablo García-Triviño, Juan P. Torreglosa, Luis M. Fernández-Ramírez,Senior Member, IEEE,and Francisco Jurado,Senior Member, IEEE

[4] H.   Yin,   C.   Zhao,   M.   Li,   C.   Ma,   and   M.   Y.   Chow,   “A   gametheory   approach   to   energy   management   of   an   engine   genera-tor/battery/ultracapacitor hybrid energy system,”IEEE Transactions onIndustrial Electronics, vol. 63, no. 7, pp. 4266–4277, 2016.

[5]   W.  Tushar,  W.  Saad,  H.  Poor,  and  D.  Smith,  “Economics  of  electricvehicle charging: A game theoretic approach,”IEEE Trans. Smart Grid

[6]A. A. Kulkarni and U. V. Shanbhag, “On the variational equilibrium asa refinement of the generalized Nash equilibrium,”Automatica, vol. 48,no. 1, pp. 45–55, 2012

[7] Oxford Dictionary . 2020 <https://www.lexico.com/definition/nash_equilibrium>
