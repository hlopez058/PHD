# Peer-to-Peer Energy Trading for Photo-Voltaic Prosumers
Hector K. Lopez, hlopez5@fau.edu, Florida Atlantic University, 119 Pennock Trace Dr. Jupiter, FL 33458

Dr. Ali Zilouchian, zilouchi@fau.edu, Department of Electrical Engineering and Computer Science, Florida Atlantic University, Boca Raton, FL 33431


I. Introduction

Net metering allows residential and commercial customers who generate their own electricity from solar power to sell the excess electricity back into the grid. Many states have passed net metering laws. Utilities may offer net metering programs voluntarily or as a result of regulatory decisions. Differences between state legislation, regulatory decisions and implementation policies mean that the mechanism for compensating solar customers varies widely across the United States. Florida law requires net metering customers are compensated at the retail rate, so FPL customers are credited for the energy produced by their solar systems at their electricity rate. As of June 2017, this was 10.8 cents/kWh for residential customers using less than 1,000 kWh each month. Home solar installations are typically Tier 1. Net metering policies create a smoother demand curve for electricity and allow utilities to better manage their peak electricity loads. By encouraging generation near the point of consumption, net metering also reduces the strain on distribution systems and prevents losses in long-distance electricity transmission and distribution. Net metering can also be seen as subsidies for affluent residents that can afford costly solar isntallations. The utilities must pay at retail electricity prices and forego the cost of maintaining the transmission and distribution infrastructure of the grid. The overhead is then shifted to other rate-payers that are unable to leverage net metering to offset energy costs. As more homes transition to solar generation the net metering incentives will need reform to support energy management of the grid.

(what are some alternatives to netmetering?)
Feed-in tarriffs
Time oF Use
Simple Tarriff


- Utah abondoning netmetering ...

- time-of-use (TOU) conditions were introduced to the reimbursements, which will see a greater value placed on energy produced and sold during times of greater energy demand.
- The system has significant economic and power potential, as it enables domestic producers to adapt their energy production and purchases based on hourly shifts in the supply, demand, and price of electricity. A 2019 report from the International Renewable Energy Agency (IRENA) found that in a pilot study in Sweden, the proportion of energy consumed during expensive peak hours fell from 23% to 19% over two years, cutting electricity spend for homeowners and reducing the burden on energy utilities at peak times.

- While feed-in tariffs, TOU systems, and battery investment represent increased phases of solar subsidy complexity that Utah

 https://www.seia.org/initiatives/net-metering#:~:text=Unfortunately%2C%20some%20utilities,as%20a%C2%A0whole.



Technological changes have made decentralized markets
feasible and attractive. Decentralized market platforms are
more compatible with both quantitative and qualitative value creation from DERs. Combined with the decline of both
solar PV costs and smart grid-enabled transaction costs,
alternatives to regulated pricing structures are preferable

The other component of a future decentralized-market platform is standard interconnection with an open architecture;
interoperability at the edge of the network; and transparent,
agreed-upon technical standards for interconnection. The
essential key to all of these charges is that the algorithms
for calculating them be transparent, consistent and communicated and applied consistently and clearly to all market
participants

Many states are considering revising net metering altogether
and instead compensating customers with a value-of-solar
tariff (VOST). The VOST takes into account all the costs and
benefits of grid-tied distributed-energy resources, including
contributions to fixed costs, avoided capital expenditures,
environmental externalities and others. A VOST dissociates
the excess generation payment to customer-generators from
the retail rate.72



II. System Configuration and Modeling
    The proposed PV-Based prosumer network consists of two main layers, the physical layer and the virtual layer. The physical layer is made of three major systems, the generation system, the metering system and the communications system. The virtual layer is made up of three major components, messaging, pricing, and billing. The physical and virtual layer are introduced in detail in this section.
        A. Physical Layer
            The physical layer of the prosumer network is comprised of the generation system installed by every prosumer, the metering hardware that measures the energy flow and the communication network that sends the messages to the other nodes on the network.
            i. Generation System
                - PV systems in florida have similar restrictions for installment
                - Modeling Residential PV Installation 
                    - Tier 1 system in Florida is maxed out at 10kW for resdiential customers
                    - Compliance with the National Electrical Code
                    - The system (unless it has a battery backup) must shut down in the case of an FPL grid outage to prevent feedback into the grid.
                    - Systems using battery storage must have a coupled DC inverter.
                    - Electrical and mechanical inspection approved by the local inspector, including details regarding the location and construction of the system.
                    - Systems must either have a U.L. 1741 listed inverter or a visible manual disconnect switch.
                    - Systems must have a bi-directional meter installed by FPL.
                    - MPPT on PV system would force it to follow the weather patterns for generation
                - PV, DC/AC converter, MPTT, Grid Disconnect Switch
                - frequency regulation needs to be correct.
                - reasons for PV tier 1 in florida?
                - modeling of typical PV system for prosumer?
                - model of the PV system and how it integrates with the prosumer load and grid
            ii. Metering System
                - Interconnection policies
                - AMI Meter , form factor with AMI addon, Meter with minimal losses?
                - model of the meter that will be connected to the home
                - what is the error int his system?
                - what type of home shall this be installed on?
                - what are the constraints of the meter? what energy can it measure?
                - details around the metering capabilities?
                - is it special when measuring bi-directionally?
                - is it cost effective?
                - how is it secured?
                - is it available on the market today?
                - how is it smarter than a regular system?
                - how would it be serviced?
                - assumptions made for somethign like this?
                - why this doesnt exist?
                - refer to some regulations here?
            iii. Communication System
                - Wireless backhaul of data using existing systems. LTE, radio, IoT LTE-M, blue wireless?
                - cost analysis of lte-m iot?
                - reliability?
        B. Virtual Layer
            i. Messaging
                - IoT,MQTT, SCADA data, industrial systems
                - Examples of Wireless IoT Data systems
                - data management 
                - security of messages
            ii. Pricing
                - pricing strategies vs NRG-X-Change, bidding?
            iii. Billing
                - distributed ledger? crypto?
                - NRGCoin
                - interledger
III. 

    


## Outline

What is the problem we are trying to solve?
Peer to peer energy trading platforms that can be used are complex and require blockchain solutions
Can a non-blockchain solution be used?
- it would need to be backed by a utility to manage security
    - Why?
        - Security concerns in blockchain can be addressed with a secure hardware and privacy overhead?
- Would it be cost effective for the utility?
- How would it be managed by the community?
    - a community managed application? 
    - hardware from a utility?
    - 

Implementation of blockchain network for NRG-X-Change?



## Abstract 
This paper reviews a peer-to-peer energy market for prosumers of a regulated utility. Utilities pay retail prices to prosumers regardless of demand, forcing utilities to pass the cost of distribution to other consumers. As prosumers grow in numbers, utilities need a better compensation method. A real-time peer-to-peer energy market application may provide higher incentives. Utilities adopt the service because it would allow for compensation of overhead. By including the utility, a micro-grid is not needed for a peer-to-peer market. The prosumer community can be virtual. The proposed implementation can become an intermediary step to decentralized energy markets. 

## Keywords
Peer-to-Peer, Energy, Markets, NRG-X-Change, Utility, Renewables, Phot-Voltaic, Distribution Service Operator, Micro-grid, Blockchain, MQTT, Industrial, Smart Metering, Florida Power& Light, Net Metering, Prosumers, Cloud computing

## Introduction 
In 2015, the Paris Agreement presented global ambitions to balance anthropogenic emissions of the planet. The focus of the agreement was to remove sources and sinks of greenhouse gases in the second half of this century. By deploying large-scale renewable energy (RE) supplies the emission of fossil fuels would be reduced. Broader climate initiatives drive the increased adoption of RE technologies. As a result, by 2030, the carbon emissions are estimated to be reduced by 40% of the levels in 1990, as shown in Fig. 1. These advances have been driven by innovations in resource management, government regulations, and demand-side management [1]. It has also been a driving force in radical reductions of solar photovoltaics (PV) panels. PV accounts for the highest change in cost [2] due to improved efficiencies, material costs, economies of scale as well as public and private R&D [3] [4].

Figure 1

Increased adoption of renewable energy technologies due to regulatory push  to reduce carbon emissions.
The PV cost reduction trends are expected to continue further in the future [5]. Many homes are now equipped with PV, electric vehicles (EV), batteries, or other equipment [6] [7]. These homes are also connected to a smart-grid technology allowing for bi-directional flow of energy, transforming these consumers into prosumers, producing energy, not just consuming it [8]. With the emergence of prosumers, local Peer-to-Peer (P2P) energy transactions have been proposed as new markets allowing direct energy trading between prosumers [9], [10]. Various trade models and clearing mechanisms for P2P energy markets have been reported [6], [11]. The benefit of a P2P energy market is to remove the intermediaries to optimize energy transactions. Despite its benefits to the electrical grid and industry, the P2P energy trading market encounters numerous challenges. The most significant challenges include the indeterminate number of unknown peers, market-clearing mechanism, payment system, trust, and transparency [12]. Instead of creating designs that require new infrastructure and processes, this paper proposes an intermediate solution by leveraging existing smart-metering hardware, real-time demand pricing strategies and community-managed cloud application.

## Related Works
Numerous studies on P2P energy trading have focused on blockchain-based P2P energy trading market designs. The blockchain is the principal technology to support many untrustworthy peer-to-peer financial services [13]. Furthermore, blockchain offers excellent opportunities to tackle privacy and fraud-related concerns in a P2P electrical energy market [14]. A practical implementation of a blockchain energy market was placed into commercial operation by LO3 Energy, in Brooklyn, New York at the start of 2016 [15]. The project enabled a citizen with PV panels on the roof of his building sold his excess electricity to his neighbor instead of feeding it to the power grid using the blockchain smart contract. This scheme allowed renewable energy producers to establish P2P connections with consumers by eliminating intermediaries. Today, numerous studies have proposed using this technology in P2P energy trading markets at consumer and transmission levels [16] [17]. Prosumers intend to participate actively in the market and propose bids for energy based on forecasting load and generation. The advantages of this market-based control concept are that it achieves close to optimal allocation, neatly balances supply and demand, and aligns preferences of self-interested prosumers [18]. However, Bidding for energy ahead of time relies heavily on predictions of future supply or order, the inaccuracy of which translates to higher costs for both buyers and sellers. In addition, prosumers need to rely on advanced trading strategies to maximize profit (or minimize costs). Also, separate energy balancing needs to be employed to cope with real-time demand response [19]. The financial incentives of a fully decentralized blockchain for the P2P energy market have yet to be proven. The lack of mainstream adoption has relegated these solutions to niche markets and micro-grid architectures [15]. A blockchain P2P energy market that leverages market-based energy trade reduces the dependency on a Distribution System Operator (DSO). The system can match demand directly between individual agents, resulting in a more decentralized and competitive environment. But removing the DSO hampers adoption of the technology. The DSO can aid in managing enrollment, security, and privacy of the market [20]. An intermediate solution is also possible. The DSO could facilitate a more profitable prosumer market and retain operational costs better than a traditional net-metering payment system [21]. 

## Contributions
This paper proposes a hardware and software solution to enable distributed communication amongst prosumer networks. The hardware solution can be implemented on the current smart metering infrastructure by the DSO, and the software solution is based on open-source technologies on ubiquitous cloud computing technologies. The paper also proposes real-time pricing strategies such as NRG-X-Change instead of traditional market-based energy trading. The real-time pricing would consider the real-time pricing of the DSO for retail energy and allow a hybrid market between prosumer networks and the DSO that could be more financially advantageous for the DSO and prosumers compared to traditional NEM subsidies. This P2P energy trading platform is analyzed by synthesizing real-world data (EIA.gov) [22] for known service territories and the associated retail price of energy as defined by the DSO. 

Paper Organization
The following Section 2 consist of an overview of the Net Metering compensation mechanism for prosumers. By comparing the Net Metering payments with the Peer-to-Peer market payments, the reader may understand the benefits of the P2P market compensations. Subsections of Section 2, dive deeper into the advent of Net Metering and its application specifically in the regulated Florida energy market. In Section 3 an overview of the various types of Peer-to-Peer markets is presented. The features of the Peer-to-Peer transactions can manifest into several configurations and can range from fully decentralized to a community managed system. Examples of existing Peer-to-Peer market projects are provided in subsections of Section 3. Section 4 dives into the design of a Peer-to-Peer market. The design choices for a Peer-to-Peer that includes the utility is laid out in contrast to popular blockchain based fully decentralized Peer-to-Peer markets. The design includes how the system would work and operate. The hardware assumptions are laid out for the metering, communications, and hosted market application. Section 5 is a technical implementation of the design. Details on how the software was architected and the implementation of the NRG-X-Change algorithm in python are provided. Finally, in Section 6 , a simulation of prosumers is created utilizing real-world data over the course of a year in 2020-2021 for the FPL territory. The prosumer data is used in a network of 3 prosumers and a network of 100 prosumers to visualize the revenue benefit of randomly synthesized load and generation profiles. The prosumer load and generation were statistically varied from real-world ensemble data from EIA.gov [2]. The paper concludes the previous chapters in Section 8, the conclusion. 

Net Metering Overview
The Advent of Net Metering
Net Energy Metering (NEM) is a compensation mechanism to encourage the adoption of residential PV systems, commonly referred to as net metering. It allowed the flow of energy to feedback into the utility grid, forcing the negative pricing of electricity to be paid back to the user [23]. The utility would have excess generation from the home that could compensate for the load of neighbors nearby. NEM encouraged consumers to spend money on PV systems without government subsidies. Prosumers with PV could reduce fossil fuels' need and overall electricity cost to ratepayers. The idea spread gradually in the 1980s. In 1981, the Arizona Corporation Commission approved net metering below 100 kW, the first among US public utility commissions (PUC). The following year, the Massachusetts PUC followed suit. In 1983, Minnesota became the first US state to enact a net metering law. More state PUCs and legislatures followed suit: the Indiana and Rhode Island PUCs in 1985, the Idaho and Texas PUCs in 1986, the Maine PUC in 1987, and the New Mexico and Oklahoma commissions in 1988 [24]. NEM has been widely implemented currently; 41 states, in addition to Washington, DC, American Samoa, US Virgin Islands, and Puerto Rico, have mandatory net metering policies. Some utilities have voluntarily offered NEM arrangements to customers, as well. For example, Idaho and Texas do not have compulsory NEM policies, but some utilities in those states do offer NEM [25]. Many utilities saw NEM break the business model and often lobby against the payback at retail prices because it does not include the transmission losses and operating costs taken on the utility. Despite the benefits of NEM, it can also be seen as a form of “cost-shifting” or subsidy for those who invest in renewables, while others who are unable to invest in it take the cost burden [26]. In conclusion, prosumers benefit from NEM, and utilities are forced to implement NEM by Public Commissions in varying states. The retail price of electricity is not ideal as a payback price for the utilities and forces them to lobby to make it more difficult for PV adoption. 
Net Metering in Florida
This paper focuses on the "Sunshine" state in America, Florida. Unlike California, the adoption of PV systems has been less aggressive because of the historically low electricity prices compared to PV costs. At the end of 2019, Florida ranked fifth in the nation in total solar power generating capacity, and utility- and small-scale solar installations contributed more than one-half of the state's renewable-sourced net generation. Although Florida is one of the nation's top electricity producers, it does not produce enough electricity to meet its power needs. Florida is the third-largest electricity consumer in the country, after Texas and California, and electricity demand is expected to increase in the years ahead as the state's population continues to grow [27]. The residential sector, where more than nine in ten Florida households use electricity as their primary energy source for home heating and air conditioning, consumes more than half of the electricity used in Florida. As a result, the residential DG market for Floridians is significant [27]. The utilities must compete with roof-top solar as it becomes more ubiquitous in the state. Traditional NEM policies may push utilities to become burdened with distribution overhead and have less revenue from ratepayers.  The Public Service Commission requires utilities to buy back electricity from prosumers at retail prices in Florida. The NEM programs for each utility provide customers with payment for credits not used to offset energy bills by the end of the year. The main utilities in Florida are Florida Power and Light Company (FPL), Tampa Electric Company (TECO), Gulf Power, and Duke Energy [27]. FPL and the other utilities allow customers to install DG systems that generate up to a certain amount based on a tiered structure. The systems cannot be sized to produce energy exceeding 115% of the annual consumption [28]. Florida law requires that net metering customers are compensated at the retail rate [28]. Utilities break up the usage of PV systems into tiers to control the amount of capacity and create safety constraints around PV installations. There are three tiers by system size; Tier 1 is 10 kW, and below, Tier 2 is above 10 kW up to 100 kW, and Tier 3 is above 100 kW up to 2,000 kW. Most prosumer homes will fall within Tier 1 due to their low installation cost and limited liability. A typical prosumer in Florida would be a Tier 1 prosumer with a system of less than 10kW of capacity. This paper leverages the prosumer constraints in Florida as guidelines to synthesize possible prosumers in the service area. Most importantly, the prosumers' excess energy would be reimbursed for the capable generation of prosumer and the retail price of energy. To this end, the paper shall focus on the FPL utility as the DSO for the simulated prosumers. FPL's average retail energy price has been 12 cents/kWh for the last ten years [22]. Furthermore, according to a survey from the US Energy Information Administration in 2018, homes in the FPL service territory had an average monthly energy usage of 1,110 kWh [22]. In conclusion, the typical prosumer in FPL's service territory would have a generation capacity of less than 10kW, an average consumption of 1,110 kWh a month. Therefore, it would be paid back about 12 cents/kWh for any excess energy generated over a year.



Peer-to-Peer Market Overview
P2P Energy Market Layers
The typical P2P market consists of a physical layer and a virtual layer. The physical layer is the infrastructure that facilitates the generation and metering of energy for the prosumer network. A prosumer has an energy generation system with an inverter that converts or steps up the power to match the home's alternating current (AC) source. An isolation switch for emergencies isolates the connection to most generation systems. The entering energy from the DG system immediately supplies the home load. Any excess energy that flows in the opposite direction (into the grid) is measured by the bi-directional meter installed at the utility distribution drop. A micro-controller with wireless connectivity can relay the meter flow over a wireless communication backhaul to other controllers [33]. The virtual layer consists of software that facilitates interactions between participants in the market. It ensures that all participants have equal access to the platform's historical financial transactions. The virtual layer consists of the messaging protocol and other transmissions of the messages securely to a message broker or a distributed ledger for settlement and trading transactions [29]. 
P2P Energy Market Types
Full-P2P configurations are suitable for isolated communities where all the infrastructure is maintained through self-forming coalitions. The bilateral contracts capture both the upstream-downstream energy balance and forward market uncertainty [28]. Blockchain-based credits are used as distributed ledger accounting to facilitate privacy and fairness. In a Community-P2P, a community manager is chosen to care for privacy and fairness. The community members share common interests and goals even though they are not at the exact location [30] may work either collaboratively or competitively [9]. Participants generally trade energy through a community manager that manages exchanges outside of the community [30]. Finally, a Hybrid-P2P would leverage the best of both worlds and even create a hierarchal approach to stacking several Full-P2P configurations and managed at a larger scale by a Community-P2P commission [31]. 



Existing P2P Energy Markets
Microgrids are known as low voltage grids, which are used to supply electricity to communities that can be operated in an islanding and grid-connected mode. Microgrids can have dispatchable energy resources (DERs) and gain an advantage to continue to operate in the islanding and grid-connected mode [29]. The DERs are managed by prosumers in a microgrid and can sell energy back to the grid with a benefit from the grid. The LO3 blockchain platform has been developed as a community energy market project [34]. The members can buy and sell energy from each other with smart contracts. The Brooklyn Microgrid project used the platform to set up the virtual layer of the market as they connected the physical layer [15]. The Brooklyn Microgrid was an apartment building in New York retrofitted with roof-top solar. The residents were all consumers contributing to the generation and consumption of the microgrid. The microgrid was able to be islanded off the main power grid and service the residents in a sustainable way. It was one of the few successful pilots in North America. Unfortunately, this project has yet to create a wave of adoption across the country. In other countries, efforts around energy trading platforms have yielded varying configurations and services. The german platforms such as Enerchain and Sonnen charge monthly participation fees but provide blockchain-based networks that protect privacy [35]. Many other European solutions established pilots or flat fee participation on a platform [36]. 

Designing An Intermediate P2P Energy Market
Criteria 
As stated in related works, P2P energy markets are typically constructed using a blockchain-based system to remove the need of a central authority and then use a market-based trading strategy to determine energy prices between prosumers. This intermediate P2P market design aims to leverage the existing utility infrastructure and a real-time energy payment based on local demand. The benefit of having this design is that it can be implemented much more straightforward and possibly provide more financial benefit to prosumers than the existing and widely used NEM. 


How it Works
For P2P energy markets, a blockchain-based system is typically used to aid in managing enrollment, security, and privacy of the market [20]. The blockchain infrastructure requires added cost and complexity to establish a distributed ledger across a scalable network of prosumers. The DSO and a Community Manager could handle the physical and virtual layers, respectively. Florida has a regulated electricity market. A P2P market that can provide additional revenue outside the NEM subsidies would require a utility to have prosumers opt into the program. Prosumers would forego the payment from NEM for the amount determined by the P2P Market algorithms. Prosumers would gain the ability to sell excess energy at the minimum retail price of fuel and more depending on the demand from neighboring consumers. The consumers who are part of the network could have the retail rate of electricity reduced when there is enough excess energy. The consumers would have cheaper electricity rates while generation is available from prosumers.  
Prosumer Setup
A typical prosumer setup is shown in Fig. 2, P1 can produce energy by conditioning it and sending it to the grid, M1, and consuming C1 energy from the grid when production doesn't fully cover the home's load. A typical prosumer configuration with solar PV installation and inverter. An AMI meter is connected to the home's load and measured by the utility at M1. An inverter is an emergency isolation switch connected to the renewable energy sources behind the meter. The excess energy flows into the grid when greater than the home's load. The utility-grade meter then measures the reverse flow as the net energy of the prosumer. A typical connection to measure flow independently requires expensive and time-consuming modifications to the wiring behind the meter. A novel proposal is to utilize the existing AMI form factor and implement a plug-n-play solution with an unregulated secondary meter in-between the AMI meter and the meter-can housing. A typical AMI meter with a proposed P2P meter interface that would interface with pass-through connectors. The P2P meter contains LTE and current sensing capabilities.


A typical prosumer configuration with solar PV installation and inverter.
By first proposing a typical prosumer and defining a prosumer network model, a P2P energy market can be suggested to facilitate energy transactions between the prosumers in a network of any number of prosumers. This paper shall focus on PV only, prosumer generation sources. Future works should consider PV and energy storage capabilities for each prosumer. A typical residence with renewable power sources is connected to the authorities through an inverter that converts DC to AC. The generation simultaneously feeds the load and the grid at a point of interconnection, netting out the final usage of the home as positive or negative flow as measured by an electrical meter. 

A typical AMI meter with a proposed P2P meter interface.


A typical residence with renewable power sources  with an inverter.
The network of prosumers and consumers could be isolated behind a substation, allowing for micro-grid isolation. However, the need for micro-grid isolation is optional because the network can still act as a virtual ledger managed as an unregulated service by the utility during the regular service operation. Network of Prosumers and Consumers are feeding and receiving directly from a substation managed by a Distribution Service Operator. M number of participants on the network ranging from 1 to n number of prosumers, p, and consumers, c. 


Network of Prosumers and Consumers feeding and recieving directly from a substation managed by a Distribution Service Operator.

Prosumer PV Modeling 
The generation sources that are installed on the prosumers would most likely be PV technology because it is simple in structure, stable in performance, and does not produce any pollutants in power generation. PV systems can be scaled to cover the full load or partial load of the residence. PV panels converts solar irradiation to electric through the photoelectric effect. The power of the PV model is obtained by the multiplied model current and voltage and expressed as:  

 ( 1 )
The consideration of losses in converting the PV energy to AC by the inverter is not considered as well as other minor losses due to system constraints. The ideal generation of the PV system can be modeled to understand how a typical prosumer would respond to measured irradiance in a location over time. If a series of prosumers interacted with consumers in a network, the prosumers would be able to provide excess energy at times that the consumers would need it. The prosumer network is represented by the set of prosumers , where  is the total number of prosumers in the network.


( 2 )
 	
In a P2P market, the prosumers' excess energy is paid to the prosumer at a market price. Extra power is referred to as net energy, and it is the difference between the prosumer's load and the prosumer's generation. An individual prosumers net energy at some time x(τ), is calculated by taking the difference between load and generation of that prosumer and clamping the value to be above 0.

( 3 )
 
Prosumer Payments
The net energy must be multiplied at some time-dependent retail price to pay a prosumer for the net energy, q(τ). The retail price is dependent on time because it is a value that changes based on demand and costs to distribute power. Therefore, the retail price would also need to be in some monetary denomination per kWh.

( 4 )
 
An individual prosumers payment can also be dependent on the demand so the retail price, . Furthermore, it can be expanded to include the terms for the total generation of the network,  and the total consumption of the network, . 

( 5 )


( 6 )
Since excess energy is not valuable when there isn't anyone to consume it, payment to the prosumer should be regulated. The payment is based on the group contribution of energy to balance with the demand. To balance the supply and demand amongst a network of prosumers, we want to compensate generation and load on the network at the correct times as proposed by the NRG-X-change mechanism [37]. A prosumers payment function is to modify the maximum retail price awarded for the energy. In comparison to the need for that contribution, the individual's contribution is considered. The final price for the energy is then attributed to the prosumer at that time.

( 7 )
The  is the maximum payment for the prosumer's energy, and where a is a constant is used to tweak the payment distribution. As the disparity between the single prosumer and total load and generation could be, the scale factor should be adjusted.  Implementing a sensitivity analysis of the scaling factor a, with respect to the net energy squared, reveals that the scaling factor should be greater than or equal to the net energy squared but small enough not to become undefined. A consumer payment function is considered similarly. The prosumers or consumers required to draw energy from the network would be charged according to the demand. The price of energy increased based on the demand forcing the behavior to change for consumers who do not wish to pay for higher costs at the demanded time.  

( 8 )
 
Where  is the maximum cost of energy delivered by the DSO, when the energy supply by the prosumers is low. When the production matches consumption, the substation will charge    per kWh. 
Market Design
The NRG-X-change protocol proposes an interchange of energy transactions leveraging a DSO as an intermediary and broker for the market. The advantage of this design is that it creates more privacy for the service participants, and it gives the DSO control to implement ancillary services incentives. Approaches that leverage blockchain technology help increases security and privacy for each person on the network. However, the costly implementation of blockchain continues to be an area of research. The transactional speeds slow down as the network grows and the complexity of implementing a viable blockchain network requires expertise by the prosumers that can be more costly than the service. To keep costs low hybrid P2P architecture is proposed. Prosumers would have a community manager initiate a software application with a reliable cloud hosting vendor under an organizational account. The market transactions would occur entirely on the market application. The metered energy flow would be sent to the application, and a centralized ledger would be kept of the payment and cost for the energy on the network. Payment for each prosumer is calculated in real-time by the broker using the NRG-X-change algorithm and recorded to provide the settlement to the prosumer and consumers participating in the network. 


Prosumers and consumers smart meters send energy flow to P2P broker.
Implementation
A proposed implementation of the communications of a P2P market is to include an IoT-capable meter with access to a wireless cellular connection. The meter would measure the power in kilowatts consumed or produced at the interconnection point with the grid. The meter would then send messages to the P2P broker. The messages are sent over the proposed P2P meter using a wireless backhaul such as LTE-M or LTE. Each P2P meter would send messages over an OASIS standard messaging protocol for the Internet of Things (IoT) called MQTT. It is designed as an extremely lightweight publish/subscribe messaging transport ideal for connecting remote devices with a small code footprint and minimal network bandwidth [38]. The messages contain a simple record structure to identify the Customer Id and the kilowatts associated with the meter. Finally, a timestamp would be sent along with the message to track the flow of energy accurately. The messages arrive at the publicly available MQTT broker endpoint. The messages are then sorted by timestamp into a stream and processed to determine each customer's payment or billing amount at every associated timestamp. At any given time, the balance of the customers would be available on a management portal.
 

Simplified flow chart of P2P application leveraging NRG-X-Change algorithm for prosumer payment and billing. 
Message Structure
The MQTT messages are encoded as binary messages. The P2P meter would send the values to the broker as an encoded string with any series of information within it.  The simulation could be simplified, JSON (JavaScript Object Notation) is used to define a message structure. An additional proposed feature that is not normal for IoT operations is the use of a "quality" code value. The quality code is used in industrial protocols to define the low-level health status of devices. These quality codes are well defined in Industrial Control System protocols such as OPC, OPC-UA, and DNP3. The quality of a given OPC tag is used to represent the validity of the tag's value (in other words, whether a client can trust the data). OPC quality is divided into three main categories: Good (generally indicates the information is valid), Bad (indicates the data type is not correct), or Uncertain (indicates the data type is speculative in some manner). Each category is further divided into sub-categories; the exact criteria for using a particular sub-category may vary depending on the end protocol and vendor.  The value for the timestamp should be chosen to be a point in time counter type time designation to avoid issues with time zones such as the Unix time (also known as Epoch time, Posix time) that is widely used in operating systems and file formats. Finally, the value for the energy is chosen to be a positive or negative value defined as a floating-point value of kilowatt.

{
    'time': 1637984408,
    'qos': 0,
    'id': 1,
    'kW': 0.12,
}
JSON formatted P2P meter message structure with sample values for each field.
Message Structure
The records arrive on the message broker in asynchronous order. The MQTT protocol allows for the messages to arrive at a given 'topic' that any MQTT client can subscribe to and listen to messages as they arrive on the topic. The published messages are available for the subscribed client. The client subscription requires the defined broker endpoint, the port that is typically 1883, and a name for the connecting client. An example of the mosquito MQTT application is shown to indicate how a user can test the submission of the message through a command line.
 

mosquitto_pub -t INFO -m '{"time": 1637984408, "qos": 0, "id": 2, "kW": 0.173}'
Example of a paho mosquitto MQTT command to publish a test message.
P2P Broker Awaiting Messages
A more exhaustive script is if leverages the Paho MQTT Python library to simulate a subscription to the broker at the given topic. The main method handles the long-running task and loops forever, expecting messages from the broker from P2P meters. The override function 'on_connect' determines what happens when a successful connection is established. 

import threading
import paho.mqtt.client as mqtt
import json
import pandas as pd
import time
mqttBroker = "localhost"
mqttPort = 1883  # port for mosquitto broker
client = mqtt.Client("p2p-broker")  # new instance
msg_dict = []  # create a list to store the messages


def main():
    # Define callback function for success connection
    client.on_connect = on_connect
    # Define callback function for receipt of a message
    client.on_message = on_message
    # Connect to the broker
    client.connect(mqttBroker, mqttPort, 60)
    # Start networking daemon 
    client.loop_forever()  

def on_connect(client, userdata, flags, rc):
print("Connected with result code {0}".format(str(rc)))
    client.subscribe("INFO")


Python script showing the main entry point for an MQTT client.
The client also overrides the "on_message" method to perform the processing of the incoming messages. The process converts the binary string into a JSON formatted object and stores it in a thread-safe list. A separate thread is invoked that loops every few seconds and processes the messages into the total production and total consumption grouped by the time interval. The methods also remove duplicate messages from the broker based on timestamp and customer Id. This forces the messages to be unique. Note that the synchronization of messages from each meter is not considered. The assumption is that all messages will arrive at a synchronized clock rate, i.e., once per second. If the messages are out of sync, the energy supplied, or consumed aggregation may not be as accurate. Aggregating a common time window or even creating back casting methods to smooth errors would result in more robust energy attribution across the network.

def on_message(client, userdata, msg):
    # convert msg to json
    data = json.loads(msg.payload)
    # check if data is in dict
    if not any(msg['time'] == data['time'] and
        msg['id'] == data['id'] for msg in msg_dict):
        # store data in a dictionary
        msg_dict.append(data)

def thread_process_msgs(id):
    while True:
     try:
        df = pd.DataFrame.from_records(msg_dict)
        tp = df[df['kW'] > 0].
                groupby(['time']).sum()
        tc = df[df['kW'] < 0].
                   groupby(['time']).sum()
        # itterate through values of tp
        for index, row in tp.iterrows():
            # update df with tp at time index
            df.loc[df['time'] == index, 'tp'] = row['kW']
        for index, row in tc.iterrows():
            # update df with tc at time index
            df.loc[df['time'] == index, 'tc'] = row['kW']
            time.sleep(2)
        df = calculate_nrg(df)
        
        except Exception as e:
            print(e)


Python methods demonstrating a threaded process that reads messages.
P2P Broker Calculating NRG-X-Change 
The payment and billing functions as described by the NRG-X-Change [21] algorithms are implemented on a central broker then provided to consumers as the final payment or bill that should be issued. This method is simpler than creating a blockchain-based network and is a lower cost and lower complexity implementation for decentralization. The payment calculation is done on the P2P broker at a configured rate. The configuration for the scaling factor and the max price of produced and consumed energy must be set by the community manager of the P2P network. In this example, the defaults are set in the script based on historical max and min pricing from the synthesized dataset.

 
# NRGXChange Payment g(.) Function
# price : the maximum price for energy produced
# tp : the total production of the network
# tc : the total consumption of the network
# a : scaling function
# n : number of particpants on the network
def g(price, X, tp, tc, a, n):
    q = price
    try:
        pay = (pow(X, n)*q)/math.exp(pow((tp-tc), 2)/a)
    except OverflowError:
        pay = float('inf')
    return pay

# NRGXChange Charge h(.) Function
# price : the maximum price for energy consumed
# tp : the total production of the network
# tc : the total consumption of the network
def h(price, Y, tp, tc):
    r = (0.01*price)
    try:
        cost = (Y*r*tc)/(tc+tp)
    except OverflowError:
        cost = float('inf')
    return cost

Python scripted payment and cost functions for prosumers and consumers conversion.
P2P Broker Management and Visualization
Cloud services provide scalable, reliable, robust solutions that can be secured for privacy. A containerized approach to the application would allow the application to be hosted on any cloud vendor. The P2P application would manage each prosumer's enrollment, pricing, and settlement of the energy. By allowing the application to be configured, the community manager can adjust max retail electricity costs and payments from the DSO. The architecture utilizes MQTT to facilitate a publish/subscribe style of communication. The transaction of the system is brokered and recorded through various microservices. The design can be scaled and distributed across agents. They were leveraging the scalability of the cloud to support a growing P2P network. The architecture can be described as a monitoring and management stack with a transactional layer.
Monitoring Stack:
It comprises open-source software that reads in messages through Filebeat. In addition, this agent can receive MQTT messages from a MQTT broker on the transactional layer and relay it to Elastic, an open-source unstructured database. The final component is Kibana, a dashboard visualization application that could provide event-level details of each event for monitoring. 
 

Elastic dashboard showing customer IDs and their energy flow in kWh.
The management stack is used to implement management roles such as enrollment, configurations, and adjustment. It can also host a public website as a portal for participants to see the balance and adjust account settings. This layer relays all changes to the MQTT broker asynchronously to the monitoring stack. The most critical component is the "Broker”, a customs agent that performs the energy balancing and ancillary energy management services between all the network participants.
	Transactional layer:
A layer that facilitates communications between participants and the management and monitoring stacks. It is made of MQTT broker that is opensource by Mosquitto.org. The exchange information can be asynchronous and passed rapidly using "publish" and "subscribe" transactional messages between the participants and the stacks. This methodology allows for distributed communications.
 


Microservice based software architecture diagram for P2P market application.
 Simulation Results
To simulate the results of the system, data was synthesized from annual consumption trends and the regulatory constraints of the geographical region of Florida. The assumptions around the size and limits of PV systems were considered based on EIA.gov [22] and NREL (National Research Energy Labs) sources. The synthesized data was then used to generate prosumers' payback for a network of N=3 prosumers and a network of N=100 prosumers. The prosumers would consume a load first and then provide any excess generation. The variations in generation and consumption are modeled with a statistic variance to cover variations in home sizes, location, losses, and other performance considerations. Future works would consider integrating energy storage alongside the PV generation that could offset generation capacity allowing for more significant revenue opportunities.  
Synthesizing Data for Florida Prosumers
The data used in the simulation is provided by the US Energy Information Administration [22].  The dataset is filtered for the Florida Power and Light service territory. The two datasets requested are for load demand and solar generation. The prosumers' load demand must be derived statistically since an individual's load is not made available through public datasets. The average use of a single prosumer can be inferred at a monthly time range but not at a daily or hourly time. The average monthly estimate for a prosumer in the FPL territory; 1,110 kWh/month. The hourly and monthly load demand is publicly available data, but it is aggregate. To use this data, normalize the aggregate usage over a time window, then multiply the estimated mean usage by each of the normalized samples over the time window. The result would be a load demand curve that estimates a typical prosumer load demand about the average load. The 1100kWh per month was divided by 730 hours to arrive at a 1.5kW load at each hourly sample. The normalized curve was mapped against the load with two standard deviations as an error. 

Two Month Hourly load demand (kWh) about an average prosumers load of (1100kWh/730h) with an error band.
 
The daily load demand of a typical consumer draws an average of 1100kWh a month correlated to the normalized curve of overall order between January 2020 and the end of February 2020. The approximation provides a starting point to model a prosumers daily consumption. The prosumers' consumption variance is considered two standard deviations from the mean but can be adjusted in future research. The actual load demand of individual users can be utilized instead of this approximation into the model for better results. In this research, we will assume the prosumers utilize PV, but this can be adjusted to be different types of generation with different driving renewable energy curves. The total solar generation of the FPL territory is an indicator of the potential capacity of a prosumers much smaller generation. The assumption is that the total correlation of solar generation on aggregate is proportional to the solar generation at the prosumer level. 

Daily load demand of a typical consumer that draws an average of 1100kWh a month.
Prosumer Network Revenue 
The analysis shows the positive and negative transactions for the energy generated by each prosumer. The prosumer revenue for id=3 generated the most revenue for the year. The analysis shows that with only PV the network is dependent on variance in load and generation performance. At larger networks, the income per prosumer tends to decrease. The variance in performance for each prosumer works against the revenue gains for each prosumer across the network.


Hypothetical generation of Prosumers in a network of N=3 using NRG-X-Change mechanisim.

Hypothetical generation of Prosumers in a network of N=100 using NRG-X-Change mechanisim.

 Conclusions
The growth of renewable energy technologies has pushed the adoption of residential solar. Regulated utilities such as FPL, pay prosumers retail prices for the excess energy. The repayment of prosumers by utilities is known as net-metering. Net-metering has promoted the growth of prosumers in states with high electricity prices. But, by subsidizing prosumers, utilities have passed the operational costs to other consumers. Researchers have proposed better prosumer compensation methods using peer-to-peer markets. The dynamic pricing could offer higher incentives at moments of peak demands that could lead to gains for prosumers.
The paper reviews an implementation where the utility is part of the market. The utility would provide the service to prosumers and consumers instead of net-metering, allowing for fair payment of overhead charges and greater pay-out to prosumers. An open-source application was created to allow for management of prosumer transactions. The application would receive messages from metering devices. The metering devices could be provided by the utility using a low-cost form factor. The connected meters would send messages to the application that over a wireless backhaul. The messages would be received by the internet hosted application. This paper simulated the consumption and generation of prosumers over the course of a year. The prosumer simulations act as a network of prosumers that generate excess energy. The excess energy follows the real-world PV generation of Florida prosumers. The simulated prosumer generation had statistical variations from the base, in line with Tier 1 PV systems. The results of prosumer networks of size three and size one hundred where provided. The results indicated the annual revenue for prosumers paid in the traditional net-metering. And the results showed how prosumers were paid on the proposed peer-to-peer application before expenses.


References



