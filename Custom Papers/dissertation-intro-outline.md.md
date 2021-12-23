           

**Review of Trustless Peer-to-Peer Distributed Energy Trading Platforms**

Hector Lopez  
8/12/21

**Introduction**

In this chapter a brief overview of how the bulk electric grid operates and its history is provided. Potential challenges in the current distribution networks are discussed. An introduction into a peer-to-peer (P2P) energy trading solution is provided. Finally the motivation is presented with a broader outline of the covered topics and the structure of the document.

**1.1 History of the Market**

The electric utility industry was first founded in 1879, and has been subject to many municipal, state and federal regulation since then. The electric utilities are considered "natural monopolies" because the efficiency in production would be higher when a single firm supplies the entire market. [1] ([[Custom Papers/References#Regulation of Natural Monopoly]]) In 1935 the United States congress passed a law to regulate the electric utilities at the state level. The Public Utility Holding Company Act (PUHCA) [2] ([[Custom Papers/References#Regime Change and Corruption A History of Public Utility Regulation]]) enforced state regulation making the utility companies incorporate in the same state they were operating in. They also owned the monopoly of that market and were forced to set prices based on the "fair rate of return". [3] ([[Custom Papers/References#Making competition work in electricity]])Then, from 1940s to1960s, the electric industry grew rapidly because of demand in energy usage. The increase in usage created environmental concerns as well as concerns over dependency on foreign oil. Regulation to limit emissions and to reduce oil usage led to the 1978 Public Utility Regulatory Policy Act (PURPA) [4].([[Custom Papers/References#Public Utility Regulatory Policies]]) The law was designed to promote the adoption of renewable resources and efficient generation. [Custom Papers/References > Regime Change and Corruption A History of Public Utility Regulation](app://obsidian.md/Custom%20Papers/References#Regime%20Change%20and%20Corruption%20A%20History%20of%20Public%20Utility%20Regulation)

The most interesting component was that it also forced utilities to buy power from independent companies that could produce power for less than what it would have cost the utility to generate the power called "avoided cost", promoting competition into the power generation business. [Custom Papers/References > Power Struggles Explaining Deregulatory Reforms in Electricity Markets](app://obsidian.md/Custom%20Papers/References#Power%20Struggles%20Explaining%20Deregulatory%20Reforms%20in%20Electricity%20Markets)  
A new class of exempt wholesale generators prompted the expansion of the Federal Energy Regulatory Commission (FERC) to initiate open transmission access. The independent generators could now dive deeper into renewable generation across the country. By the 1990s the most prominent initiative was in the California Power Exchange (PX), a regional spot market for buyers and sellers to trade electricity. [Custom Papers/References > The California Energy Crisis](app://obsidian.md/Custom%20Papers/References#The%20California%20Energy%20Crisis) The California ISO was started in 1990 and was designed to operate the state’s power transmission grid and provide open access to all qualified users. [Custom Papers/References > Cost of Service Regulation In the Investor-Owned Electric Utility Industry A History of Adaptation](app://obsidian.md/Custom%20Papers/References#Cost%20of%20Service%20Regulation%20In%20the%20Investor-Owned%20Electric%20Utility%20Industry%20A%20History%20of%20Adaptation)

Even with competition in the market the PX prices remained high because of collusion by power producers and power brokers. Order 888 by FERC was passed to introduce competition at a wholesale level, but the market had fluctuating prices and resulted in an energy crisis. [Custom Papers/References > A quantitative analysis of pricing behavior in California’s wholesale electricity market during summer 2000](app://obsidian.md/Custom%20Papers/References#A%20quantitative%20analysis%20of%20pricing%20behaviour%20in%20California%E2%80%99s%20wholesale%20electricity%20market%20during%20summer%202000) Manipulation of the market by nefarious companies such as Enron, led to stricter regulation around how the market should operate. The requirements for the market to be more flexible and capable of integrating renewables is also an inevitable challenge. [Custom Papers/References > The California Electricity Crisis Causes and Policy Options](app://obsidian.md/Custom%20Papers/References#The%20California%20Electricity%20Crisis%20Causes%20and%20Policy%20Options)

**1.2 The Smart Grid**

“The grid” refers to the electric grid that consists of a network of transmission lines, substations, transformers, etc. which transfer the electricity from the power plant to the home or business. [Custom Papers/References > Application of Cooperative Game Theory in Smart Grids](app://obsidian.md/Custom%20Papers/References#Application%20of%20Cooperative%20Game%20Theory%20in%20Smart%20Grids) The average age of power plants in north America is 35 years old. Also, more than half of the electricity in north America is generated through coal and the delivery efficiency of electricity is an abysmal 35%. Finally, frequent and major blackouts in the past indicate critical vulnerabilities in the electrical infrastructure. [Custom Papers/References > The smart grid - where are we today and what the future holds](app://obsidian.md/Custom%20Papers/References#The%20smart%20grid%20-%20where%20are%20we%20today%20and%20what%20the%20future%20holds)

The challenges of creating a more efficient grid led to the adoption of smart management systems that can intelligently integrate the actions of all users connected to it, including generators, consumers and those that do both in order to efficiently deliver sustainable, economic and secure electricity supplies. [Custom Papers/References](app://obsidian.md/Custom%20Papers/References) The result is a "Smart grid", an advanced power system that integrates the electrical network with smart digital communication technology. Providing bi-directional communication between the utility and consumers, leveraging smart sensors across the system. [Custom Papers/References](app://obsidian.md/Custom%20Papers/References)

**1.3 Challenges for the Grid**

Conventional electric power systems in most countries have been designed so that a central power station produces electrical power. Then transformers increase the voltage to high levels which are suitable for transmission. Once the energy arrives at a community the voltage is gradually stepped down to lower levels into the distribution network until it is finally dropped into the consumer’s premise. The energy is then measured by a meter that keeps record of the energy consumption in real-time. [Custom Papers/References > The Power of Change Innovation for Development and Deployment of Increasingly Clean Electric Power Technologies](app://obsidian.md/Custom%20Papers/References#The%20Power%20of%20Change%20Innovation%20for%20Development%20and%20Deployment%20of%20Increasingly%20Clean%20Electric%20Power%20Technologies) The flow of electricity was traditionally uni-directional but in the age of distributed generation the grid must also deal with bi-directional flow back to the grid from producers who used to just be customers.

The Smart Grid must grow to incorporate the bi-directional flow of electricity between supply and demand sources as penetration of Plug-in Electric Vehicles (PEVs) and distributed energy resources (DERs) like Photo-voltaic Solar Panels, (PV) increases in residential sectors. The American Recovery and Reinvestment Act of 2009 (ARRA) [Custom Papers/References > Smart Grid – The New and Improved Power Grid A Survey](app://obsidian.md/Custom%20Papers/References#Smart%20Grid%20%E2%80%93%20The%20New%20and%20Improved%20Power%20Grid%20A%20Survey) was designed to address the smart grid transition improving in the following areas :

-   Reliability – the reliability of grid will be improved by several factors including less disturbances and blackouts.
-   Economics – by reducing the electricity rates and creating new jobs and enhancing the U.S. gross domestic product.
-   Efficiency – by reducing the costs associated with generation, transmission and distribution of the electricity.
-   Environmental – by reducing the number of emissions by increasing the integration of renewable resources.
-   Security – by reducing the probability of manmade attacks and natural disasters.
-   Safety – by reducing the consequences of any grid-related events

The reliability, economics and efficiency of the grid will improve as communication technologies transition into advanced implementations of hardened sensor networks across the grid known as the industrial internet of things (IIoT). [Custom Papers/References > Internet of Things IoT and the Energy Sector](app://obsidian.md/Custom%20Papers/References#Internet%20of%20Things%20IoT%20and%20the%20Energy%20Sector) The IIoT improvements to the grid can affect the energy generation efficiency, demand side management and even the transmission and distribution of energy for energy carriers. The more data the grid provides in real-time allows for optimization leading to greater reliability and efficiency, reducing the cost of electricity. [Custom Papers/References > Internet of Things in industries A survey](app://obsidian.md/Custom%20Papers/References#Internet%20of%20Things%20in%20industries%20A%20survey)

The environmental, safety, and security aspects of the grid will improve as the adoption of distributed generation and energy storage improves. DG systems are typically renewable as roof-top solar (PV) . The environmental benefits of renewables in the short term are attractive but there is still an environmental cost to create PV technology. [Custom Papers/References](app://obsidian.md/Custom%20Papers/References) The distribution of generation and adoption of microgrids could decentralize the security risk of the current grid improving its overall-reliability and increasing resiliency.

The overall challenges of the smart grid are many, but driving technological trends seem to point to a redesign of the infrastructure and the market structure that operates it. The increase of DG and renewables with the increase of retail electric prices and the decreasing of profitable incentive tariff rates are all challenges for the grid. [Custom Papers/References > Peer-to-Peer Energy Trading in Electrical Distribution Networks](app://obsidian.md/Custom%20Papers/References#Peer-to-Peer%20Energy%20Trading%20in%20Electrical%20Distribution%20Networks)

**1.4 Overview of Peer-to-Peer**

With the increasing connection of renewable energy sources, traditional energy consumers are becoming prosumers, who can both consume and generate energy [Custom Papers/References > Autonomous Cooperative Energy Trading Between Prosumers for Microgrid Systems](app://obsidian.md/Custom%20Papers/References#Autonomous%20Cooperative%20Energy%20Trading%20Between%20Prosumers%20for%20Microgrid%20Systems). Peer-to-Peer (P2P) energy trading has emerged as a next-generation energy management mechanism for the smart grid that enables each prosumer of the network to participate in energy trading with other prosumers and the grid. [Custom Papers/References > Transforming energy networks via peer-to-peer energy trading The potential of game-theoretic approaches](app://obsidian.md/Custom%20Papers/References#Transforming%20energy%20networks%20via%20peer-to-peer%20energy%20trading%20The%20potential%20of%20game-theoretic%20approaches)

Renewable energy sources are usually intermittent and difficult to predict. When prosumers have surplus electricity, they can curtail it, store it with energy storage devices, export it back to the power grid, or sell it to other energy consumers. The direct energy trading among consumers and prosumers is called peer-to-peer energy trading, which was developed based on the “P2P economy” concept (also known as sharing economy) [Custom Papers/References > The Sharing Economy Why People Participate in Collaborative Consumption](app://obsidian.md/Custom%20Papers/References#The%20Sharing%20Economy%20Why%20People%20Participate%20in%20Collaborative%20Consumption), and is usually implemented within a local electricity distribution system.

**1.5 Motivation**

The P2P energy trading markets have a virtual, and physical layer. As a potential solution to the growth of the grid it is a promising topic of research. Research into the various challenges presented by the latest literature is provided with accompanying potential solutions for those challenges. Areas of interests are :

-   Different energy market structures
-   Reducing the cost of energy usage
-   Increasing and maintaining sustainable use of renewables
-   Improving social engagement of prosumers
-   Constraints by the power network
-   Can not violate the voltage limit at prosumers nodes
-   Reduction of overall network loss

The following chapters dive deeper into existing energy market structures then presents the Peer-to-Peer market structure in varying forms. The concept of Peer-to-peer is broken down into virtual and physical layers. Further explanation of each layer and the challenges for each is presented for the reader. A recreation of the "Elecbay" distributed market trading platform is presented leveraging a MQTT protocol implementation for use with Internet of Things devices. [Custom Papers/References > Internet of Things-aided Smart Grid Technologies Architectures Applications](app://obsidian.md/Custom%20Papers/References#Internet%20of%20Things-aided%20Smart%20Grid%20Technologies%20Architectures%20Applications) Simulation of market dynamics on the platform are studied by presenting game theoretic approaches for P2P energy trading as feasible and effective means of energy management. [Custom Papers/References > Transforming energy networks via peer-to-peer energy trading The potential of game-theoretic approaches](app://obsidian.md/Custom%20Papers/References#Transforming%20energy%20networks%20via%20peer-to-peer%20energy%20trading%20The%20potential%20of%20game-theoretic%20approaches) A blockchain enabled IIoT approach using re-enforcement learning is presented to improve security of financial transactions on the network. Finally, Future work is gathered for each of these topics and presented for the reader.

**Peer-To-Peer Network**

**2.1 Overview of the Network Elements**

P2P networks can be divided into two layers:

1.  Virtual layer
2.  Physical layer

The virtual layer essentially provides a secured connection for participants to decide on their energy trading parameters. It ensures that all participants have equal access to a virtual platform. The virtual platform facilitates the transfer of buy and sell orders, and financial transactions. The physical layer is a physical network that facilitates the transfer of electricity from sellers to buyers once the financial settlements between both parties are completed over the virtual layer platform. It can be a traditional distributed-grid network maintained by the independent system operator or an additional separate physical microgrid distribution grid, in conjunction with the traditional grid. [Custom Papers/References > Transforming energy networks via peer-to-peer energy trading The potential of game-theoretic approaches](app://obsidian.md/Custom%20Papers/References#Transforming%20energy%20networks%20via%20peer-to-peer%20energy%20trading%20The%20potential%20of%20game-theoretic%20approaches)

**2.2 Overview of Market Structure**

Market operations of a P2P network consists of payment rules, and a clearly defined bidding format. The main objective is to enable an efficient energy trading process by matching the sell and buy orders in near real-time granularity. In market operations the generation of each producer influences the thresholds of maximum and minimum energy allocation. Different market-time horizons may exist in the market operation that should be able to produce enough allocation at every stage of operation. [Custom Papers/References > Peer-to-Peer Trading in Electricity Networks An Overview](app://obsidian.md/Custom%20Papers/References#Peer-to-Peer%20Trading%20in%20Electricity%20Networks%20An%20Overview)

**Fully Decentralized Market**

Fully decentralized markets allow for prosumers to independently and directly negotiate with each other to decide on energy trading parameters without any centralized supervision by leveraging bilateral contracts between prosumers.  
In a fully decentralized market the bilateral contracts capture both the upstream-downstream energy balance as well as forward market uncertainty. [Custom Papers/References > Bilateral contract networks for peer-to-peer energy trading](app://obsidian.md/Custom%20Papers/References#Bilateral%20contract%20networks%20for%20peer-to-peer%20energy%20trading)

**Community Based Market**

Community-based market can be applied to community microgrids and group of neighboring prosumers. The members of the community share common interests and goals even though they are not at the same location. [Custom Papers/References > Peer-to-peer and community-based markets A comprehensive review](app://obsidian.md/Custom%20Papers/References#Peer-to-peer%20and%20community-based%20markets%20A%20comprehensive%20review) They may work either in a collaborative or competitive manner. [Custom Papers/References > Energy storage sharing in smart grid A modified auction-based approach](app://obsidian.md/Custom%20Papers/References#Energy%20storage%20sharing%20in%20smart%20grid%20A%20modified%20auction-based%20approach) Participants generally trade energy through a community manager. The community manager manages exchanges outside of the community. Privacy is preserved by the community manager. [Custom Papers/References > Peer-to-peer energy trading in a prosumer-based community microgrid A game-theoretic model](app://obsidian.md/Custom%20Papers/References#Peer-to-peer%20energy%20trading%20in%20a%20prosumer-based%20community%20microgrid%20A%20game-theoretic%20model)

**Composite Market**

Composite market combines the fully decentralized and community-based market designs. An individual prosumer can engage in P2P trading between each other, while also interacting with existing markets like fully distributed markets. [Custom Papers/References > Online energy sharing for nanogrid clusters A Lyapunov optimization approach](app://obsidian.md/Custom%20Papers/References#Online%20energy%20sharing%20for%20nanogrid%20clusters%20A%20Lyapunov%20optimization%20approach) Community manager can also oversee trading inside the community. [Custom Papers/References > A sustainable home energy prosumerchain methodology with energy tags over the blockchain](app://obsidian.md/Custom%20Papers/References#A%20sustainable%20home%20energy%20prosumerchain%20methodology%20with%20energy%20tags%20over%20the%20blockchain)

**2.3 Overview of Existing Challenges**

The challenges for the physical layer of P2P is the integration of sensors and smart power systems that can support flexible loads and dynamic generation. The penetration of DERs and energy storage currently provide insignificant shifts in the overall grid operation but will soon grow into more substantial impacts if trends in technology persist. [Custom Papers/References > Transforming energy networks via peer-to-peer energy trading The potential of game-theoretic approaches](app://obsidian.md/Custom%20Papers/References#Transforming%20energy%20networks%20via%20peer-to-peer%20energy%20trading%20The%20potential%20of%20game-theoretic%20approaches) The virtual layer for P2P trading hinges on the information system that communicates the transactions between physical layer and in-between participants.

The P2P Information system needs to be able to:

1.  enable all market participants to communicate with one another for participating in energy trading;
2.  integrate the participants within a suitable market platform;
3.  give the participants equal access to the market;
4.  monitor the market operation;
5.  set restrictions on participant's decisions to ensure network security and reliability.

Examples of information systems for P2P networks include blockchain-based smart contracts [Custom Papers/References > Local electricity storage for blockchainbased energy trading in industrial Internet of Things](app://obsidian.md/Custom%20Papers/References#Local%20electricity%20storage%20for%20blockchainbased%20energy%20trading%20in%20industrial%20Internet%20of%20Things), consortium blockchain [Custom Papers/References > Consortium blockchain for secure energy trading in industrial internet of things](app://obsidian.md/Custom%20Papers/References#Consortium%20blockchain%20for%20secure%20energy%20trading%20in%20industrial%20internet%20of%20things), and Elecbay. [Custom Papers/References > Peer-to-Peer energy trading in a Microgrid](app://obsidian.md/Custom%20Papers/References#Peer-to-Peer%20energy%20trading%20in%20a%20Microgrid)

**Design of a P2P Energy Trading Platform**

**3.1 Overview of Elecbay**

A P2P energy trading platform "Elecbay" was designed for a grid-connected low-voltage (LV) Microgrid. The simulation of P2P bidding among energy consumers and prosumers through the energy trading platform "Elecbay" was developed using game theory. [Custom Papers/References > Peer-to-Peer energy trading in a Microgrid](app://obsidian.md/Custom%20Papers/References#Peer-to-Peer%20energy%20trading%20in%20a%20Microgrid) Trading through “Elecbay” is competitive, which means energy consumers and prosumers are not aggregated with each other for achieving higher benefits via co-operation. Energy consumers and prosumers are considered as “good citizens”, who contribute to maintaining local energy balance.

The typical process flow is as follows:

1.  Energy sellers list the items (i.e the surplus energy over half an hour for sale.)
2.  Energy buyers browse all the listed items and then place orders
3.  Orders are placed by peers and are accepted or rejected by Elecbay, DSO, and energy suppliers.
4.  Energy is delivered through the distribution network and peers generate/consume the amount of energy as promised in the accepted orders.
5.  The actual energy generation and consumption is recorded by smart meters in real-time so that the Elecbay can provide energy balancing services.
6.  Financial settlement transactions are processed by Elecbay to the participants.

Each order contains details of the buyer and seller, time period, price of energy and the energy exchange amount. The acceptance of the orders is based on network constraints, voltage excursion, thermal overloading, etc. In an ideal world the energy can always be balanced but when it can’t Elecbay needs to provide penalties to the peers who fail to generate/consume the promised amount of energy. The penalties can arise in higher prices for future orders. Elecbay collects service charges and eventually pays out to the DSOs, energy sellers and energy buyers during a settlement period. [Custom Papers/References > Peer-to-peer energy market for community microgrids](app://obsidian.md/Custom%20Papers/References#Peer-to-peer%20energy%20market%20for%20community%20microgrids)

**3.2 Implementing 'Open-Elecbay'**

Elecbay software proposed by Zhang [Custom Papers/References > Peer-to-Peer energy trading in a Microgrid](app://obsidian.md/Custom%20Papers/References#Peer-to-Peer%20energy%20trading%20in%20a%20Microgrid) indicated the platforms purpose to primarily facilitate trading within a micro-grid. The implementation of the software by a community would need to be managed by a community manager of some kind and the associated communication infrastructure would also need to be in place.

Open-Elecbay: A proposal for an architecture that handles streaming IoT data sets from multiple clients requesting independent bids/offers on the market. The architecture utilizes MQTT and existing IOT protocol to facilitate a publish/subscribe style of communication. The transaction of the system is brokered and recorded through various microservices. The design can be scaled and distributed across agents.

**Micro-Services and Containerization for the Cloud**

The author proposes a software implementation that leverages containerization to increase its portability into managed cloud services. This method would facilitate a scalable, reliable, resilient solution reducing overhead costs instead of maintaining physical equipment.

**MQTT Protocol**

The implementation of Elecbay does not identify a particular protocol, but a proposal to use a publish and subscribe based protocol instead of the traditional industrial communication protocols can enhance the inter-operability of the platform when onboarding DERs and IoT sensing devices. Most industrial equipment will come with OPC-UA protocol compatibility. The standard provides speed, security and reliability. Modern protocols such as message queue transport telemetry (MQTT) can implement similar security by using a certificate approach. It can also be very reliable because of its eventual consistency message design. The speed of communication has also improved through modern message compression techniques. The main benefit MQTT would provide is that it is widely used in the residential IoT space. The industrial controllers for DERs are also supporting the protocol as a new standard. By allowing IoT enabled devices such as home appliances to interact with the platform.

Appliances, Energy Storage Systems, PEVs, PV panels, Lights, Water Heater, HVAC, can all interact over a standard IoT protocol and behave as individual market participants securing energy from generators based on predicted demand.

**Game-theory for P2P trading**

**4.1 Using Game-Theory in P2P**

Game and auction-theoretic models have been used in P2P energy trading as an effective means of energy management approaches. The development of P2P energy trading has the potential to substantially benefit prosumers in terms of earning revenues, reducing electricity costs, and lowering their dependency on the grid. [Custom Papers/References > Designing microgrid energy markets - A case study The Brooklyn Microgrid](app://obsidian.md/Custom%20Papers/References#Designing%20microgrid%20energy%20markets%20-%20A%20case%20study%20The%20Brooklyn%20Microgrid)

The system poses the challenge of modeling the decision-making process of each participant for the greater benefit of the entire energy network while considering human factors, e.g., rationality, motivation, and environmental friendliness. Particularly, in settings where there are many users with conflicting interests participating, it would be challenging either to integrate such conflicting interests when designing the decision-making process of each participant or, if necessary, to motivate the users to cooperate with reducing costs, maximizing revenues, and pursuing renewable energy objectives. [Custom Papers/References > Transforming energy networks via peer-to-peer energy trading The potential of game-theoretic approaches](app://obsidian.md/Custom%20Papers/References#Transforming%20energy%20networks%20via%20peer-to-peer%20energy%20trading%20The%20potential%20of%20game-theoretic%20approaches)

An energy management solution is needed that provides efficient and robust operation considering the conflicting nature of energy trading. Game theory should be a very effective tool for modeling the decision-making process of participants.

**4.2 Basic Game-Theoretic Concepts**

Game theory is a mathematical and signal processing tool that analyzes [Custom Papers/References > Economics of electric vehicle charging A game theoretic approach](app://obsidian.md/Custom%20Papers/References#Economics%20of%20electric%20vehicle%20charging%20A%20game%20theoretic%20approach) strategies in competitive solutions where the outcome of a participants choice is based on the actions of other participants. There are two main branches: 1. noncooperative and 2. cooperative game theory.

**Non-Cooperative games**

These types of games allow players to take necessary action, to make optimal decisions, without any coordination or communication with each other. Noncooperative games can be further divided into 'static' or 'dynamic' games.

-   Static game: Players act only once, either simultaneously or at different times. An example could be two business owners deciding where to open a new store location.
-   Dynamic game: Players act more than once and have input regarding the choices of other players. Time can play a central role in these games. Dynamic games can be modeled as a series of static games, but time and information would need to be reflected in the utility functions. An example of a dynamic game would be Chess.

For both types of non-cooperative games, the players will make decisions based on "pure strategy" a deterministic way, or a probabilistic way "mixed strategy". [Custom Papers/References > Transforming energy networks via peer-to-peer energy trading The potential of game-theoretic approaches](app://obsidian.md/Custom%20Papers/References#Transforming%20energy%20networks%20via%20peer-to-peer%20energy%20trading%20The%20potential%20of%20game-theoretic%20approaches) The most popular concept in non-cooperative games is the solution concept called the Nash equilibrium. It refers to a stable state of a non-cooperative game where neither player can improve its utility by unilaterally altering its action when other players actions are fixed. An example in the game of Monopoly is when there are no more actions the player can make with the money on hand that could better the situation. A Nash equilibrium always exists in a game with mixed strategies (probabilistic decisions) but not always guaranteed in pure strategies (deterministic). Finally the non-cooperative game may have multiple Nash equilibriums and the most desirable one should be chosen for the solution. [Custom Papers/References > Noncooperative and cooperative optimization of electric vehicle charging under demand uncertainty A robust stackelberg game](app://obsidian.md/Custom%20Papers/References#Noncooperative%20and%20cooperative%20optimization%20of%20electric%20vehicle%20charging%20under%20demand%20uncertainty%20A%20robust%20stackelberg%20game)

**Cooperative games**

-   Canonical Coalitional game:
-   Coalition Formation game:
-   Coalition Graph game:

**4.3 Game-Theoretic Applications for P2P**

The application of game theory in energy trading and management is extensive. However, the discussion of its application in the field of P2P energy trading is limited, which could be because of the relatively recent emergence and exploration of P2P trading frameworks in energy domains [Custom Papers/References > Transforming energy networks via peer-to-peer energy trading The potential of game-theoretic approaches](app://obsidian.md/Custom%20Papers/References#Transforming%20energy%20networks%20via%20peer-to-peer%20energy%20trading%20The%20potential%20of%20game-theoretic%20approaches)

**Coalitional Energy Trading**

If small scale electricity suppliers and consumers are participants on the network and are connected on the physical layer through local distribution that can be islanded off, then there is potential for trading energy in an isolated fashion. The discrepancy between the wholesale price and retail price matters because the peer-to-peer trading price will be greater than the wholesale price but less than the retail price. The consumers will always want to trade with a peer because it would be cheaper than retail energy traveling over long transmission lines. The local prosumers would also benefit from the trading price being more than the wholesale price of creating the electricity and therefore gaining profit. [Custom Papers/References > Direct electricity trading in smart grid A coalitional game analysis](app://obsidian.md/Custom%20Papers/References#Direct%20electricity%20trading%20in%20smart%20grid%20A%20coalitional%20game%20analysis)

The coalition formed between prosumers is a canonical coalitional game with transferable utility, and the price for P2P energy trading is determined by an asymptomatic Shapley value [Custom Papers/References > Coalitional game theory for communication networks](app://obsidian.md/Custom%20Papers/References#Coalitional%20game%20theory%20for%20communication%20networks). The net surplus of the coalition is sold to the retail market at wholesale prices but bought at retail prices if there is a net deficiency. The coalition can then effectively ban together to optimize the return on energy generated and consumed by trading with each other before selling or purchasing from the grid.

There are only 10 states that still pay the wholesale price (avoided cost) when selling back to the grid. All other states pay retail price to sell to the grid. In these states the super additivity of the grand coalition is no longer viable and there is no reason to stay in the coalition. [Custom Papers/References > Net Metering is a Win-Win for Utilities and Local Communities](app://obsidian.md/Custom%20Papers/References#Net%20Metering%20is%20a%20Win-Win%20for%20Utilities%20and%20Local%20Communities) An avoided cost (also known as net-metering) is the minimum amount an electric utility is required to pay an independent power producer, under the PURPA regulations of 1978, equal to the costs the utility calculates it avoids in not having to produce that power (usually substantially less than the retail price charged by the utility for power it sells to customers).

**Day-Ahead Optimization**

With a view toward reducing the cost of energy trading within the grid, a day-ahead optimization process regulated by an independent central unit has been proposed in [Custom Papers/References > Demand-side management via distributed energy generation and storage optimization](app://obsidian.md/Custom%20Papers/References#Demand-side%20management%20via%20distributed%20energy%20generation%20and%20storage%20optimization). The existence of optimal strategies is proven, and, furthermore, the authors present a distributed algorithm to be run on the users’ smart meters, which provides optimal energy-production and storage strategies while preserving user privacy and minimizing required central unit communication.

**Auction Games for DERs**

Auction games have been proposed for trading both storage space and renewable energy from DERs [Custom Papers/References > Energy storage sharing in smart grid A modified auction-based approach](app://obsidian.md/Custom%20Papers/References#Energy%20storage%20sharing%20in%20smart%20grid%20A%20modified%20auction-based%20approach). The real-time implementation of a multiagent-based game-theoretic reverse auction model for microgrid market operations featuring conventional and renewable DERs is discussed. [Custom Papers/References > Real-time implementation of multiagent-based game theory reverse auction model for microgrid market operation](app://obsidian.md/Custom%20Papers/References#Real-time%20implementation%20of%20multiagent-based%20game%20theory%20reverse%20auction%20model%20for%20microgrid%20market%20operation) The proposed methodology was realistically implemented in a smart grid system at Florida International University, and the subsequent investigation shows that the proposed algorithm and the industrial hardware-based infrastructure are suitable for implementation in the existing electric utility grid.

Meanwhile, the authors in [Custom Papers/References > Energy storage sharing in smart grid A modified auction-based approach](app://obsidian.md/Custom%20Papers/References#Energy%20storage%20sharing%20in%20smart%20grid%20A%20modified%20auction-based%20approach) utilize an auction game to study the solution of joint-energy-storage ownership sharing between multiple shared facility controllers (SFCs) and those dwelling in a residential community. The auction process possesses both incentive-compatibility and individual-rationality properties and is also capable of enabling the residential units (RUs) to decide the fraction of their shared energy storage capacity with the SFCs of the community to assist in storing electricity

For example, in [Custom Papers/References > Direct electricity trading in smart grid A coalitional game analysis](app://obsidian.md/Custom%20Papers/References#Direct%20electricity%20trading%20in%20smart%20grid%20A%20coalitional%20game%20analysis) a coalitional game is used to study the cooperation between small-scale DERs and energy users to enable the direct trading of energy without going through retailers. The asymptotic Shapley value is the core of the coalitional game so that no small-scale DERs or energy users have an incentive to abandon the coalition, which suggests the stable direct trading of energy for the proposed pricing scheme. Furthermore, numerous case studies demonstrate that the scheme is suitable for practical implementation. The authors in [Custom Papers/References > Economic power transaction using coalitional game strategy in micro-grids](app://obsidian.md/Custom%20Papers/References#Economic%20power%20transaction%20using%20coalitional%20game%20strategy%20in%20micro-grids) focus on comprehensive economic power transactions of multiple microgrid networks with multiple agents; they design a three-stage algorithm based on a coalitional game strategy and include request, exchange, merge-and-split, and cooperative transaction stages. The developed algorithm enables microgrids to form coalitions where each microgrid can exchange power directly by paying a transmission fee.

**Blockchain for P2P**

When communicating between many participants an encrypted form of communication can be used to secure transactions between the participants. They all work towards processing the message and providing a consensus on what the message between any two participants should be. This consensus across all participants is crucial for trustless systems. In P2P networks a blockchain messaging mechanism can be used to validate financial transactions on a distributed ledger, it can also be used to track energy usage without the fear of tampering with the metering information over the air. The attack would need to achieve 51% control of the network in order to approve the false transactions. In an unsecure network the attack would only need to override a single node and create false readings for a meter or a financial transaction. In a federated system the operator would oversee securing the infrastructure and communications. But in an open P2P network design cryptographic methods such as blockchain provide unfederated security, privacy and protection against the network.

**Optimization for IIoT**

In the description of blockchain networks are provided, with the 4 tradeoffs. The paper goes on to describe how optimization for IIoT transactions was achieved using the Gini Coefficient for fairness. The scope of network size and performance is provided and proven to show the efficacy of the proposed optimization method for these networks to be sufficient. Different consensus models are also provided with benchmarked analysis of the performance .[Custom Papers/References > Performance Optimization for Blockchain-Enabled Industrial](app://obsidian.md/Custom%20Papers/References#Performance%20Optimization%20for%20Blockchain-Enabled%20Industrial)

We seek to find similar optimization for the P2P transactions in terms of IIoT communications and in terms of system criticality over peak times.

**Consensus with Distributed Energy Management**

A consensus energy management approach is discussed with a possibility to provide additional privacy to participants on the network. [Consensus Network Based Distributed Energy Management for PV-Based Charging Station](app://obsidian.md/Consensus%20Network%20Based%20Distributed%20Energy%20Management%20for%20PV-Based%20Charging%20Station).

**Conclusion**

-   Describe topics in general
-   Highlight novel contributions

-   Redesign of Elecbay for Cloud/IoT systems
-   Critical review of Coalitional Game for P2P trading with and without Net-Metering policies
-   A fluctuating blockchain optimization to match forecasted network congestion from energy profile

-   Discuss results

**Discussion of Future Research Direction**

-   Network Charge Identification
-   Large Scale Network trading and simulation
-   Benefit to the grid
-   Ancillary Service to the grid (virtual power plants)
-   Multi-level storage management
-   Prioritizing stakeholders
-   Injection limit and market mechanism
-   Unified model
-   Enabling data accessibility with privacy (using the anonymous gaming algorithms to hide information on the energy trading platform?)
-   Inter and Intra-community trading