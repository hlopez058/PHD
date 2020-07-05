
## Reading List:

1. Internet of Things (IoT) and the Energy Sector
Naser Hossein Motlagh 1 , Mahsa Mohammadrezaei 2 and Julian Hunt 3 and Behnam Zakeri 3,4,*

2. Internet of Things-aided Smart Grid: Technologies,
Architectures, Applications, Prototypes, and Future
Research Directions
Yasir Saleem, Student Member, IEEE, Noel Crespi, Senior Member, IEEE, Mubashir Husain Rehmani, Senior Member, IEEE, and Rebecca Copeland

3. A Software Defined Fog Node Based Distributed Blockchain Cloud Architecture for IoT
P. K. Sharma, M. Chen and J. H. Park, "A Software Defined Fog Node Based Distributed Blockchain Cloud Architecture for IoT," in IEEE Access, vol. 6, pp. 115-124, 2018, doi: 10.1109/ACCESS.2017.2757955.

4. System Planning of Grid-Connected Electric Vehicle Charging Stations and Key Technologies: A Review
Chao-Tsung Ma, Department of Electrical Engineering, CEECS, National United University, Miaoli 36063, Taiwan; ctma@nuu.edu.tw; Tel.: +886-37-382482; Fax: +886-37-382488; Received: 13 October 2019; Accepted: 1 November 2019; Published: 4 November 2019

5. Distributed energy storage node controller and control strategy based on energy storage cloud platform architecture
Yu Yang,Student Member, IEEE, Qing-Shan Jia,Senior Member, IEEE, Xiaohong Guan,Fellow, IEEE,Xuan Zhang, Zhifeng Qiu,Member, IEEE, and Geert Deconinck,Senior Member, IEEE

6. Decentralized EV-Based Charging OptimizationWith Building Integrated Wind EnergyYu Yang,Student Member, IEEE, Qing-Shan Jia,Senior Member, IEEE, Xiaohong Guan,Fellow, IEEE,Xuan Zhang, Zhifeng Qiu,Member, IEEE, and Geert Deconinck,Senior Member, IEEE



## Decentralized EV-Based Charging OptimizationWith Building Integrated Wind Energy: Review

by Hector Lopez 6/10/20

Major Takeaway : This is not a practical design for implementing wind turbines on every building. lots of issues.

How can i use the optimization techniques in this paper?

-  EV based decentralized charging algorithm EBDC
- Model predictive control
- Numerically demonstrates the EV charging demand and wind power suppy of buildings is scalable using EBDC
- can this approach be suitable for a wind site? should each wind turbine have a battery?
- main contributions
	- real time coordination of EV charging,with weather forecast and Model Predictive control
	- EV decentralized charging algorithm. 
	- Comparison of hueristic and optimal control
- EV;s scheduling techniques
	- charging cost reduction
	- load flattening
	- frequency regulation
	- waiting time minimization
- EV parking with solar , controled by a central system operator.
	- day ahead must be accurately predicted
- Markov decision is best to attach the EV charging problem. his  approach  can  take  advantageof the Markov property of the problem; however, it is usuallyintractable  due  to  the  state  and the  action  space  explosion
- The  spatial-temporal  charging  flexibility  related  to  themobility of EVs [32], [33] has been scarcely addressed in theliterature,


Detail Notes :
- Departure from a buildling to another building was graphed out to be gaussian distributed around a major time, of 8:30am
- I reearched the MPC approach, and studied what this controller model could fo. 
- The EBDC apporach they created showed a local optimization based on announced price - Combine these methods with event based optimization to handle wind and or solar renewable energy?
- can i create a distributed controller for wind and energy and storage sites?
- 




## Review:Distributed energy storage node controller and control strategy based on energy storage cloud platform architecture

by Hector Lopez 6/9/20

### Summary
The paper tries to present a method to manage storage systems that are independent from eacho ther. An objective function is created with the idea to minimize charing prizs. 

### Notes
- plug and play device
- intelligent power consumption mode
- Load perception of the power grid
- operating state and service life of distributd energy storage devices
- Integrated optimal control scheme
- Energy optimization and deployment strategy for stratified partition
- rduce operating costs of energy storage device on client side
- Suzhou client-side distributed energy storage demo
- Problem:
	- Strong decentralization
	- Difficult Control
	- Inconsistent aggregation paramters of dis. sustem
	- Hogh overall oepration cost





## Review: System Planning of Grid-Connected Electric Vehicle Charging Stations and Key Technologies
Chao-Tsung Ma

by Hector Lopez 6/8/20


### Summary
The paper is a digest of many algorithms bieng applied to the problem of EVintegration with the grid. It highlights each algorithm in the major problems , like power transer rate, poer and energy management, and system optimization.
The interesting challenges around optimizing the distributed behavior is solved using swarm optimization and game theory techniques for economic transactions as well as infrastructure and power arbitrage.
The paper makes th case that Renewable generation will be adopted when EV's can help balance the dynamic nature of the demand curve through proper energy storage and smooting. They explain that EV's are a complicated and multi-layered subject that can range from smart home technologies to economics to power converter systems. Each niche having its unique research and optimization strategies.

Action Items :  
- Define Topics of Interest
- Can we implement same methodology for different "generation tehcnology"




### Notes
- EV supply equipment is expected to increase 
- Problems to overcome 
	- power trabsfer rate
	- power and energy mangement
	- system optimization
- EV grid-tied with renewable energy requires control schemes
- V2G can smooth fluctuating power an enable the onboarding of more renewables on the grid
-  a 50kw ECS simulaiton showd that an ecs caued minimal harmonic distortion 
- Tandem queing model was used to manage commercial potential of an ECS network of 4 vehicles
- Placement of charging stations was optimized using shared nearest nighbor clustering algorithm
- Swarm optimization algorithm was used to solve optimization of ECS capacity placement
- Multi-objective evolutionary algorithm to optimize planning of an ECS infrastructure
- Benders decomposition algorithm to optimize the charging schedule of an ECS with a battery swapping service


## Review: Internet of Things (IoT) and the Energy Sector
Naser Hossein Motlagh 1 , Mahsa Mohammadrezaei 2 and Julian Hunt 3 and Behnam Zakeri 3,4,*

by Hector Lopez 6/1/20

### Summary
The paper highlights the future of research in the blockchain and green iot solutions. The paper covers the virtual powerplant idea as an aggregation of prosumers and discusses the needs for democratization of energy by tracking the distributed cost of energy consumption. Fog Computing seems to be the best way for blockchain technologies in IoT to be adopted in the energy sector because it circumvents the computational and security needs for a mature network by utilizing existing infrastructure built at wind and solar sites. The paper offers an insight into the use of IoT in the energy sector by providing the breakdown of the most important component to energy constumption, HVAC follwoed by lighting. These two components can be controlled by blockchain solutions and have a great. impact. Leading to the idea that a transformation of the grid can occur when IoT networks transform the energy sector forom a centralized supply chain into a decentralized , smart and optimized system.

### Notes
- It highlights future research to be focused on Blockhain and Green IoT solutions
- VPP is an aggregation of prosumers
- Democratization of energy will enable new ways to track and distribute cost of energy consumption
- Distributed computing techniques can increase security, and save energy in the IoT network, but crates complex architecture
- Fog computing can ease the adoption of blockchain technologies in IoT (due to the computational needs , places like wind/solar sites may have the infrastructure to provide it)
- IoT Based powerplants can save 230M , and IoT retrofitted powerplants can save 50M over the course of its lifetime
- Examples of IoT in practice :
	- Detection if Energy Demeand exceeds grid capacity
	- Optimizing consumption and generation using far-sighted strategies
	- Active voltage management to reduce Transmission and Distribution Line losses
	- Reduction of non-technical losses using smart meter network
- Half of residential energy consumption is due to HVAC 
- About 20% of residential consumption is due to lighting
- Energy solutions in the residentail space would benefit from IoT management of HVAC and Lighting systems
- Energy eindustry will transform from centralized supply chain into a decentralized, smart, and optimized 


## Review: Internet of Things-aided Smart Grid: Technologies,Architectures, Applications, Prototypes, and Future Research Directions
Yasir Saleem, Student Member, IEEE, Noel Crespi, Senior Member, IEEE, Mubashir Husain Rehmani, Senior Member, IEEE, and Rebecca Copeland

### Summary
The paper dives into a detailed breakdown of each segment of the smart grid. The survey results in acknowledging the lack of research in published prototypes of IoT network simulations. The smart grid architecture proposed shows the layers involved in the networks overlaying the digital network with the physical network of power transmission. Most of the research surveyed has been shown to be focused on the Home area networks or HAN's . IoT networks are built around mesh communications such as blue tooth and zigbee that allow for near field communications for systems dont require high-reliability. In a smart grid the HAN is the first layer that needs to be connected through a field area network (FAN) or nieghborhoood area network (NAN). The best solution for NAN's for IoT is LoraWan but its still not as useful for smart grid control because of the security concerns. The best NAN communicaiton tehcnology is a mix of cellular communication , wireless mesh and existing wired telecom lines. The WAN wide area network is best implemented with wired telecom lines to provide reliability needed by the smart grid. The greatest challenge of IoT penetration into the Smart Grid is the problem of interoperability. The different network solutoins do not have clear standard for various reasons described in the paper aorund regional and technical constraints.  The lack of standards causes manufacturers in HAN networks to adopt the best communication technology for the service or product that is provided. Compounding the problem smart grid technology will not change until there is economic demand to push the risk of grid stability into untested wireless communication technologies.


### Notes
- Information Flow can be overlaid on top of the Power Flow and labeled as WAN (Wide area network),NAN (nieghbordhood area network),HAN(Home Area Network) or FAN (field area network0, in accordance with Generation,Transmission,Distribution, and Consumption
- Electric vehicles can be charged or discharged in multiple ways when paired with a home. V2G , vehicle to grid, V2V , vehicle to vehicle, and V2H vehicle to home . All of these methods can be used by EV's to participate in the market as prosumers
- Smart Grid adds three main things to power grid
	- remote controlling and monitoring
	- reporting to consumer
	- integration of renewable and distributed energy resrouces
- Smart grid has 4 main subsystems
	- power generation
	- power transmission
	- power distribution
	- power utilization
- Smart grids with IoT enable
	- information flow
	- power flow
	- distribution flow
-Smart Grids use smart meters over General Packet Radio Service (GPRS) of other mobile networks
- Standards are not yet established for IoT aided SG
- This survey reveals that there is little literature on the application of IoT-aided SG systems in the area of power generation, transmission and utilization. The potential of renewable energy may depend, for example, on IoT-based prediction of weather conditions that can regulate energy flow between different regions, and on monitoring the efficiency of the involved equipment (solar panels, wind turbines).
- SGAM (Smart Grid Architecture Model) which is designed for SG planning and is the SG reference architecture by EU Mandate M/490
- REal time montorng of medium voltage grid, using Phase Measurng Unit PMU, adopted discrete Kalman Filter over weighted least squares for more accurate estimations 
- The discrete Kalman Filter with no control input solves the problem of estimating the state of a discrete-time system process. It is suitable for 3-phase systems and solely relies on nodal synchrophasor measurement offered by PMUs.
- his prototype validates the accuracy and time latency of a real-time 3-ph state estimation process deployed in a real Active Distribution Network (ADN)
- From this viewpoint of the prototype literature, it becomes apparent that there are no easily available open-source testbeds and simulation tools to enable developing experimentations and performance evaluation of IoT aided SG systems. For this purpose, [170] is a good source of guidance.
- for industrial applications and discussed how WirelessHART can outperform ZigBee
- NB-IoT incurs latency, so it is not suitable for delay-tolerant applications, such as distributed automation and Distributed Energy Resourc
- The powerline transmission medium of the PLC technology is noisy and harsh, increasing the challenges of channel modeling [206]. Moreover, the quality of signals are adversely affected by using powerlines in SGs due to various parameters, such as the number and types of IoT devices connected through powerlines, the wiring distance between transmitters and receivers, and the network topology [186]
- We came to know that most of the communication technologies are designed by focusing HAN. However, there is a new IoT communication technology, named LoRaWAN, which is a very good candidate for NAN and WAN and it is a long range and low-power communication technology.
- data fusion technologies to filter and aggregate only useful data from multiple IoT devices, 
- Interoper- ability is defined as the ability of two or more heterogeneous networks/devices to exchange information between them, and to use the exchanged information in a common function

## Review:A Software Defined Fog Node Based DistributedBlockchain Cloud Architecture for IoT
PRADIP KUMAR SHARMA1, MU-YEN CHEN2, AND JONG HYUK PARK1, (Member, IEEE)1Department of Computer Science and Engineering, Seoul National University of Science and Technology, Seoul 01811, South Korea2Department of Information Management, National Taichung University of Science and Technology, Taichung 404, TaiwanCorresponding author: Jong Hyuk Park (jhpark1@seoultech.ac.kr

### Summary

### Notes:
- distributed cloud architecture based on blockchain is proposed
- proposes a distributed fog node architecture using SDN
- blockchain allows for full decentralization and redundnacy
- costreductin of storage, Amazon is 25/tb hwile a block chain would cost 2/tb
- inveted a proof of service protocol for blockchain algorithm
- matchmaking algorithm asks "can i perform this task on thismachine"
- scheduler is needed in distributed computing systems 
- use a fog node to reduce securitly vulnerabilities
- use a packet parser to analyze packets for attacks
- We evaluate the proposed scheme byusing the throughput, response time and the delay-incurredperformance metrics. We also evaluate the accuracy of theproposed model by measuring the speed with which it candetect and mitigate saturation attacks at the edge of the net-work.
- tasks are ran on the closest fog node 
- We used the TFN2K tool to generate real-timeattacks. TFN2K is a well-known attack tool for generatingattacks such as ICMP, TCP / SYN, and UDP flood attacks
- In the first case, to increase the numberof hosts to 30K, we used Mininet. We then propelled faketopology, ARP poising and DDoS attacks to the blockchain-based SDN controller network fog node in the edge network.
- It is based on three emerging technologies: fog com-puting, SDN, and blockchain
- high availability, real-time data delivery,high scalability, security, resiliency, and low latency.
- It also demonstrates the efficiency and effective-ness of the proposed model and that it meets the requireddesign principles with minimal overhead.In the future, we will explore the various energy har-vesting technique aspects of our proposed model for energyefficient communication among devices at the edge of theIoT network


Power COnsumption of today:
WHat it will look like in the future;
- Hybrid Wind/solar sites as they exist today power generation
- future of powergenreation

Use the wind generation and show how we can contribute to the existing state using communication technologies
- reduce oepration 

how to control them, and how to destirbute the network communication.

how does this work HAN

Power Generation: Monitoring and Control of wind turbines and hybrid sites
- State of the art
- what are the issues in communciation and controls for wind turbines.
- how to fix?


How to connect and pay fee of car:
- figure out the stats and growth rates of car trends
- how the trends will be predicted on the generation and payment
- communication ohurdles and how to enter it?
- solutions : 
	- for tesla , change the battery in the battery stations
	- battery density increases and battery charging improves and what will the cost be?
	- how does  chearging a car help you 






## Research The Following :

Algorithm-distributed optimization, Benders decomposition,bi-level programming, Bayesian game, constraint-generation,distributionally robust optimization (DRO), game theory,generalized Benders decomposition, genetic algorithms,Lyapunov optimization, mixed integer linear programming,Monte Carlo, multi-objective optimization, multi objectivewhale optimization algorithm (MOWOA), oligopoly, particleswarm optimization (PSO), queuing theory, randomizedalgorithm, shared nearest neighbor (SNN) clusteringalgorithm, stochastic dynamic programming (SDP),stochastic programming, Voronoi diagram, wait-and-seesolution (WS)[29,31,33–37,39–42,46,51,55–57,67,68,70,74–76,80,81,83,88,90,97,100,102,107,109,112,115,117,118,124–126,131–133,137–142]

	29.Wang, S.; Bi, S.; Zhang, Y.J.A.; Huang, J. Electrical Vehicle Charging Station Profit Maximization: Admission,Pricing, and Online Scheduling.IEEE Trans. Sustain. Energy2018,9, 1722–1731. 

	31.Dong, X.; Mu, Y.; Jia, H.; Wu, J.; Yu, X. Planning of Fast EV Charging Stations on a Round Freeway.IEEETrans. Sustain. Energy2016,7, 1452–1461. 
	

	33.Luo, C.; Huang, Y.; Gupta, V. Placement of EV Charging Stations—Balancing Benefits among MultipleEntities.IEEE Trans. Smart Grid2017,8, 759–768. 

	34.Zhang, T.;  Chen, X.;  Yu, Z.;  Zhu, X.;  Shi, D. A Monte Carlo Simulation Approach to Evaluate ServiceCapacities of EV Charging and Battery Swapping Stations.IEEE Trans. Ind. Inform.2018,14, 3914–3923.

	35.Liu, Y.; Xiang, Y.; Tan, Y.; Wang, B.; Liu, J.; Yang, Z. Optimal Allocation Model for EV Charging StationsCoordinating Investor and User Benefits.IEEE Access2018,6, 36039–36049. 

	36.Wang, S.; Dong, Z.Y.; Luo, F.; Meng, K.; Zhang, Y. Stochastic Collaborative Planning of Electric VehicleCharging Stations and Power Distribution System.IEEE Trans. Ind. Inform.2018,14, 321–331. 

	37.Deb, S.; Tammi, K.; Kalita, K.; Mahanta, P. Charging Station Placement for Electric Vehicles: A Case Study ofGuwahati City, India.IEEE Access2019,7, 100270–100282. 

	39.You, P.; Yang, Z.; Chow, M.; Sun, Y. Optimal Cooperative Charging Strategy for a Smart Charging Station ofElectric Vehicles.IEEE Trans. Power Syst.2016,31, 2946–2956. 

	40.Pflaum, P.; Alamir, M.; Lamoudi, M.Y. Probabilistic Energy Management Strategy for EV Charging StationsUsing Randomized Algorithms.IEEE Trans. Control Syst. Technol.2018,26, 1099–1106. 

	41.Zhang, Y.; You, P.; Cai, L. Optimal Charging Scheduling by Pricing for EV Charging Station With DualCharging Modes.IEEE Trans. Intell. Transp. Syst.2019,20, 3386–3396. 

	42.Tan, X.; Qu, G.; Sun, B.; Li, N.; Tsang, D.H.K. Optimal Scheduling of Battery Charging Station Serving ElectricVehicles Based on Battery Swapping.IEEE Trans. Smart Grid2019,10, 1372–1384. 

	46.Graber, G.; Galdi, V.; Calderaro, V.; Mancarella, P. A Stochastic Approach to Size EV Charging Stations withSupport of Second Life Battery Storage Systems. In Proceedings of the 2017 IEEE Manchester PowerTech,Manchester, UK, 18–22 June 2017.

	51.Salapi ́c, V.; Gržani ́c, M.; Capuder, T. Optimal Sizing of Battery Storage Units Integrated into Fast ChargingEV stations. In Proceedings of the 2018 IEEE International Energy Conference (ENERGYCON), Limassol,Cyprus, 3–7 June 2018.

	55.Wang, Y.; Yang, Y.; Zhang, N.; Huang, M. An Integrated Optimization Model of Charging Station/Battery-SwapStation/Energy Storage System Considering Uncertainty.  In Proceedings of the 2017 IEEE InternationalConference on Energy Internet (ICEI), Beijing, China, 17–21 April 2017.

	56.Tan, X.; Sun, B.; Wu, Y.; Tsang, D.H.K. Asymptotic performance evaluation of battery swapping and chargingstation for electric vehicles.Perform. Eval.2018,119, 43–57. 

	57.Zhang, Y.; He, Y.; Wang, X.; Wang, Y.; Fang, C.; Xue, H.; Fang, C. Modeling of fast charging station equippedwith energy storage.Glob. Energy Interconnect.2018,1, 145–152.

	67.Lee, W.; Xiang, L.; Schober, R.; Wong, V.W.S. Electric Vehicle Charging Stations With Renewable PowerGenerators: A Game Theoretical Analysis.IEEE Trans. Smart Grid2015,6, 608–617. 
	
	68.Lee, W.; Schober, R.; Wong, V.W.S. An Analysis of Price Competition in Heterogeneous Electric VehicleCharging Stations.IEEE Trans. Smart Grid2019,10, 3990–4002. 

	70.Rui, T.; Hu, C.; Li, G.; Tao, J.; Shen, W. A distributed charging strategy based on day ahead price model forPV-powered electric vehicle charging station.Appl. Soft Comput.2019,76, 638–648. 

	74.Chen, Q.; Wang, F.; Hodge, B.M.; Zhang, J.; Li, Z.; Shafie-Khah, M.; Catalão, J.P.S. Dynamic Price VectorFormation Model-Based Automatic Demand Response Strategy for PV-Assisted EV Charging Stations.IEEE Trans. Smart Grid2017,8, 2903–2915. 

	75.Song, Y.;  Zheng, Y.;  Hill, D.J. Optimal Scheduling for EV Charging Stations in Distribution Networks:A Convexified Model.IEEE Trans. Power Syst.2017,32, 1574–1575. 

	76.Zheng, Y.; Song, Y.; Hill, D.J.; Meng, K. Online Distributed MPC-Based Optimal Scheduling for EV ChargingStations in Distribution Systems.IEEE Trans. Ind. Inform.2019,15, 638–649. 

	80.Shakerighadi, B.; Anvari-Moghaddam, A.; Ebrahimzadeh, E.; Blaabjerg, F.; Bak, C.L. A Hierarchical GameTheoretical Approach for Energy Management of Electric Vehicles and Charging Stations in Smart Grids.IEEE Access2018,6, 67223–67234. 

	81.Yan,  J.;   Menghwar,  M.;   Asghar,  E.;   Panjwani,  M.K.;   Liu,  Y.  Real-time  energy  management  for  asmart-community microgrid wi

	83.Seddig, K.; Jochem, P.; Fichtner, W. Two-stage stochastic optimization for cost-minimal charging of electricvehicles at public charging stations with photovoltaics.Appl. Energy2019,242, 769–781. 

	88.Kandil, S.M.; Farag, H.E.Z.; Shaaban, M.F.; El-Sharafy, M.Z. A combined resource allocation framework forPEVs charging stations, renewable energy resources and distributed energy storage systems.Energy2018,143, 961–972. 

	90.Li, S.;  Wu, H.;  Bai, X.;  Yang, S. Optimal Dispatch for PV-assisted Charging Station of Electric Vehicles.In Proceedings of the 2019 IEEE PES GTD Grand International Conference and Exposition Asia (GTD Asia),Bangkok, Thailand, 19–23 March 2019.

	97.Ugirumurera, J.; Haas, Z.J. Optimal Capacity Sizing for Completely Green Charging Systems for ElectricVehicles.IEEE Trans. Transp. Electrif.2017,3, 565–577. 

	100.Khanghah, B.Y.; Anvari-Moghaddam, A.; Guerrero, J.M.; Vasquez, J.C. Combined Solar Charging Stationsand Energy Storage Units Allocation for Electric Vehicles by Considering Uncertainties. In Proceedings ofthe 2017 IEEE International Conference on Environment and Electrical Engineering and 2017 IEEE Industrialand Commercial Power Systems Europe (EEEIC/I&CPS Europe), Milan, Italy, 6–9 June 2017.

	102.Xie, R.; Wei, W.; Khodayar, M.E.; Wang, J.; Mei, S. Planning Fully Renewable Powered Charging Stations onHighways: A Data-Driven Robust Optimization Approach.IEEE Trans. Transp. Electrif.2018,4, 817–830.

	107.Hilton, G.; Kiaee, M.; Bryden, T.; Cruden, A.; Mortimer, A. The case for energy storage installations at highrate EV chargers to enable solar energy integration in the UK—An optimised approach.J. Energy Storage2019,21, 435–444. 

109.Domínguez-Navarro, J.A.; Dufo-López, R.; Yusta-Loyo, J.M.; Artal-Sevil, J.S.; Bernal-Agustín, J.L. Design ofan electric vehicle fast-charging station with integration of renewable energy and storage systems.Int. J.Electr. Power Energy Syst.2019,105, 46–58. 

112.Liao, Y.; Lu, C. Dispatch of EV Charging Station Energy Resources for Sustainable Mobility.IEEE Trans.Transp. Electrif.2015,1, 86–93. 

115.Hassoune,  A.;  Khafallah,  M.;  Mesbahi,  A.;  Bouragba,  T.  Smart  Topology  of  EVs  in  a  PV-Grid  SystemBased Charging Station. In Proceedings of the 2017 International Conference on Electrical and InformationTechnologies (ICEIT), Rabat, Morocco, 15–18 November 2017.


- Select 3

Admission control, charging control, charging currentcontrol, coordinated control, direct load control, distributedcontrol, droop control, energy management, frequencyregulation, fuzzy controller, PID controller, power control,predictive control, voltage balance control (VBC), voltagecontrol, voltage loop control[28–30,36,40–44,48,64,70,73,76,77,79–82,85,90,93,105,106,108,113–115,118,119,121,123–125,127,128,131,132,135–138,140,141]

- Select 3

Clean energy, green energy, renewable energy, renewablepower, solar PV, wind
[67–69,71,72,74,85,86,88–90,92,93,95–98,101–109,111,112] 
[117–119,124,125,127,130–134,139–143]

- Select 3


Behavior, charging behavior, consumer behavior, frequencyresponse, performance evaluation, user satisfaction degree
[26,28,30,33,35,40,43,63,86,87,126,128,136]

- Select 3