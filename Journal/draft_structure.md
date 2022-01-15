Components
- Research from Fpl eia.gov?
- Providing a realtime simulation?
- NRGXChange simulation? it doesnt have a real blockhcain smart contract available, but do i need one? 
- A form factor for the AMI meter is not really hashed out.. should i elaborate on it?
- The question is , does a system like this help the utility beat netmetering?
- A better method for net metering in a regulated service territory?
- Real time peer to peer energy trading as an alternative to regulated Net-Metering Services using NRGCoin


Traditional support policies for green energy have greatly contributed to the rise in prosumer numbers. However, it is believed that they will soon start to exert negative impact on stakeholders and on the grid. Policy makers advise to phase out two of the most widely applied policies – net metering and feed-in tariff, in favor of support policies that scale better with rising renewable generation


The aim of our demonstration is threefold: (i) to raise
awareness about the challenges and impact of possible smart grid scenarios; (ii) to highlight the impact
of NRG-X-Change on green energy trade; and (iii)
to demonstrate the weather influence on monetary incentives and market behaviour.

Is net metering  
Demonstration of the NRG-X-Change on Florida Prosumers and an analysis of net metering alternative?
Can we create a demonstration of the NRG-X-Change?
Implement the NRG-X-Change?
- Build on what they have?
- Expand on it



## Contribution
- Measurement for typical Prosumer in Florida using FPL NetMetering Tier1 

## Results and Comparison

## Experimental setup and data
Experimental data is collected from EIA.gov a governmental entity in charge of collecting data on energy consumption in the United States[]. The data is cleansed and extracted for all residential solar generation that has come from the state of Florida. The data was then independently validated with generation estimates from the National Research Energy Labs (NREL) solar generation calculator[]. The data is then coupled with assumptions to disaggregated the performance of a typical home in Florida. A typical homes generation is capped at the tier level of a residential home. The largest utility in the state is Florida Power & Light, so it is used as the source for the retail cost of electricity. A typical prosumer is modeled using statistical noise applied to the aggregate curve for generation and load that was derived from the collected data and assumptions. A prosumer's statistical deviation from the norm is assumed to vary using a gaussian distributed random variable. The experiments sweeps the standard deviation between a range to simulate varying home sizes. The home sizes range in size given assumptions of typical homes sizes that could hold a typical solar installation on the roof.  

## Assumptions

In Florida a residential home can purchase and install a 10kW PV system and have it connected to the utility without many additional fees. A 10kW system is seen as a Tier 1 system by the Florida Electric Utilities. The process of installing a soalr generation system with the utility requires permitting and additional safety criteria. Adding a battery to the PV system can add additional criteria as well. In the end the generation from the PV system will offset the cost of the homes load. Florida utilities will then pay the prosumer according the the Net Metering guidelines followed byt he utility. The experimentation will reference the largest utility in Florida, Florida Power & Light, for these details. 

### Home Sizes, Usage and Generation
In general, 1 kW of solar energy can be generated from 66sq.ft. []. A 10kW solar system would need 660sq.ft. of roof space. A 10kW system is comprised of 30 to 40 panels total depending on the efficiency of the panels []. The typical size of a home in Florida is 1,375sq.ft., with varying roof configurations. It is arbitrarily assumed that the 10kW solar system would need a home roof size of 800sq.ft., ruling out smaller trailers, and mobile homes. Larger than 3,000sq.ft. homes would border on commercial needs and would exist as outliers to typical homes. Facilities designed as rental or multi-tenant structures may not have a need for such an installation as well. In conclusion a Single-Family home structure owned by a resident in Florida is best suited for a PV solar system installation of 10kW. Between 2010 to 2015 the number of homeowners in Florida living in single-family homes was on average 3.5 million []. A normal distribution of the 3.5 million homes is assumes with a minimum of 800sq.ft, median of 1,375sq.ft. and a max of 3,000sq.ft. . The relationship between the size of the home and its usage is assumed to be a linear relationship 

It is assumed that the typical prosumer will have a roof large enough to hold a solar generation system large enough to provide the most generation capacity available to a resident. According to the FPL teh largest size system a residential customer would have is 10kW. Any larger and they are considered out of the "Tier 1" status and require additional costs to have it installed. A 10kW generation system is likely to be installed on homes ranging from 800 sq.ft. to 3000 sqft. in area under roof. The size of the home also indicates the typical usage of the home. A typical home would utilize 1,078 kWh/month according to [] research. The usage of the home will vary by size so a formula to simulate these assumptions is provided below. 

### Cost of Installation
Most residents in fl



Highlights
•
Six support policies are evaluated in scenarios with various numbers of prosumers.

•
"What-if" scenarios are studied through multi-agent simulations with real data.

•
Net metering and feed-in tariff will cause issues in the immediate future.

•
Market-based support policies are a better fit when prosumer numbers rise.

•
Each policy offers different trade-offs between profits and costs for stakeholders.

> Humans consume vast amounts of energy and the growth of consumption is exponeital

Popular science articles
VUB-onderzoekers vinden cryptomunt ‘NRGcoin’ uit voor overschotten groene energie (in Dutch) – HLN.be
Des chercheurs de la VUB inventent une cryptomonnaie pour les surplus d’énergie verte (in French) – RTBF
NRGcoin: cryptocurrency voor groene energie (in Dutch) – De Tijd
Är det en teknikrevolution på gång? (in Swedish) – ETC
How Blockchain Technology Could Decentralize The Energy Grid – FastCoExist
Virtual currency for ‘prosumers’ could save EU power grids – Horizon Magazine
An Energy Blockchain for European Prosumers – Bitcoin Magazine
Baas over eigen zonnepaneel dankzij Bitcoin-techniek (in Dutch) – VUB Today
The Scanergy Project, a SCAlable and modular system for eNERGY trading between prosumers – European Energy Innovation
Digital currency for green energy can boost the renewable economy – FoCaS Reading Room
The Scanergy smart grid: Earning you more money from your solar panels – Intel IQ
Scientific publications
M. Mihaylov, I. Razo-Zapata, and A. Nowé, “NRGcoin – A Blockchain-based Reward Mechanism for Both Production and Consumption of Renewable Energy,” in Transforming Climate Finance and Green Investment with Blockchains, ISBN: 978-0128144473, Elsevier, 2018.

M. Mihaylov, R. Rădulescu, I. Razo-Zapata, S. Jurado, L. Arco, N. Avellana and A. Nowé, “Comparing Stakeholder Incentives Across State-of-the-art Renewable Support Mechanisms,” in Renewable Energy, Elsevier, 2018

M. Mihaylov, I. Razo-Zapata, R. Rădulescu, and A. Nowé, “Boosting the Renewable Energy Economy with NRGcoin,” in Proc. of the 4th International Conference on ICT for Sustainability (ICT4S), Amsterdam, The Netherlands, 2016.

M. Mihaylov, S. Jurado, N. Avellana, I. Rázo-Zapata, K. Van Moffaert, A. Cañadas, M. Bezunartea, L. Arco, I. Grau and A. Nowé, “SCANERGY: a Scalable and Modular System for Energy Trading Between Prosumers,” in Proc. of the 14th International Conference on Autonomous Agents and Multiagent Systems (AAMAS), Istanbul, Turkey, 2015.

M. Mihaylov, S. Jurado, N. Avellana, K. Van Moffaert, I. Magrans de Abril and A. Nowé, “NRGcoin: Virtual Currency for Trading of Renewable Energy in Smart Grids,” in Proc. of the 11th International Conference on the European Energy Market (EEM), Krakow, Poland, 2014.

M. Mihaylov, S. Jurado, K. Van Moffaert, N. Avellana, and A. Nowé, “NRG-X-Change: A Novel Mechanism for Trading of Renewable Energy in Smart Grids,” in Proc. of the 3rd International Conference on Smart Grids and Green IT Systems (SmartGreens), Barcelona, Spain, 2014.

M. Mihaylov, I. Razo-Zapata, R. Rădulescu, S. Jurado, N. Avellana and A. Nowé, “Smart Grid Demonstration Platform for Renewable Energy Exchange,” in Lecture Notes in Computer Science: Advances in Practical Applications of Scalable Multi-agent Systems, vol. 9662, pp 277-280, DOI: 10.1007/978-3-319-39324-7_30, 2016.

