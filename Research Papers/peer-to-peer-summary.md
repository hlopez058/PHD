# Review of Peer-to-Peer Energy Trading Platforms - 2021



# DERs


# P2P Markets
## Overview of the P2P Energy Trading System

1) *Prosumers*: The end-user who acts as a buyer or a seller in P2P energy trading. Each prosumer chooses a role according to their current energy consumption and generation. The prosumer can be a consumer or a producer.
2) *System Operator*: The system operator is the central authority of the P2P energy trading system. The system operator is responsible for the entire energy trading service. The operator can log in via the web portal and manage the overall system.
3) *Smart Controller*: The component that allows for the exchange of information in the market. Each prosumer has its own smart controller, so that it can exchange information with others in the P2P energy trading market.



## 2. Why are peer-to-peer energy markets important?

This section explains the premise in terms of economic (bilateral contracts), technology (microgrids) and social (peer-to-peer) energy markets.

### 2.1 Bilateral contracts and Microgrids

## 2.2 Research projects around P2P energy markets
- NREL (National Renewable Energy Laboratory)
- EIA (Energy Information Administration)
- Elecbay (Elecbay)
- Brooklyn LO3 (Brooklyn LO3)
- NRGCoin
- Enerchain
- Smart Watts
- NOBEL
- P2P3M
- Energy Collective

## 3. Designs for P2P energy markets

### 3.1 Full-scale P2P energy markets
- Description of the decentralized nature of full energy market
- Optimization techniques for full energy market are lagrangian relaxation, linear programming, and quadratic programming. The solutions define individual problems for each agent, while guaranteeing privacy and fairness. Only the power and price of the agent are revealed to the other agents.

### 3.2 Community-based P2P energy markets
- Description of the manager based P2P energy market model
- THe manager acts as the mediator between the agents and the market. The manager is the only one who knows the price of the energy. The manager also negotiates outside of the community.
- Members usually share a common interest in the market.
- Tushar Gupta, “Community-Based P2P Energy Markets,” in Proceedings of the 2013 ACM Conference on Computer and Communications Security, 2013, pp. 1–8.
- Implemented an auction scheme to share energy storage in a community-based P2P energy market.

### 3.3 Hybrid P2P energy markets
- Seen as a russian doll approach, where in each layer community-based P2P energy markets are combined with full-scale P2P energy markets.

### 3.4 Comparison of P2P energy markets
- Describe advantages and disadvantages of each market type.
- ICT infrastructure must sustain the market designs.
- Blockchain technology may be a key to deploy peer-to-peer energy markets.
- Advantages are data-management without third-party intermediaries, and the market is decentralized.
- These markets can also exist without blockchain technology.

## 4. Opportunities and Challenges for P2P energy markets



# Game Theory
## Models to Simulate Prosumers
### Defining a Welfare Model
A logarithmic utility function and a quadratic utility function are used to create welfare models for prosumers in P2P energy trading.

- Optimizing the power consumption and revenue of prosumer.

### Auctioneer Model
The auctioneer coordinates and manages the auction process. 
Price is a decision variable determined by the auctioneer. 

### Double Auction-Based Game Theoretic Mechanism for P2P Energy Trading
- Prosumers determine their role based on their energy generation and demand. 
- Then, prosumers register in the P2P market by submiting their bid/ask and amount of energy to the auctioneer. We note that the submitted value is always positive in terms of quantity.
- A double auction market is when a buyer's price and a seller's asking price match, and the trade proceeds at that price. Auction markets do not involve direct negotiations between individual buyers and sellers, while negotiations occur for over the counter trades.
- The traditional Vickry auction scheme is a sealed bid auction. Bidders submit their reservation prices to the auctioneer without knowing other prospective bidders' prices. The bidder with the highest reservation price is the winner but pays at the second-highest price.

1) *Auctioneer*: The coordinator, which determines the rules to reflect the number of buyers and sellers who engage in trade. It sends buyers the price during the auction process according to maximum and minimum price. Finally, it determines the precise quantity and price based on pre-defined rules. 

2) *Buyers*: The buyers submit their bid/ask price and amount of energy to the auctioneer. They have deficit demand and engage in the market to buy electricity. They expect their profit in the market to be optimized.

3) *Sellers*: The sellers submit their bid/ask price and amount of energy to the auctioneer. They have surplus demand and engage in the market to sell electricity. They provide extra energy at particular time of day and expect benefit from selling to the market instead of selling it to the main grid. 

#### Winner Determiniation Rule
During the auction process the auctioneer determines the number of buyers and sellers who can participate in trade based on a double auction. Winner determination is executed in the following manner:

1. Buyers are sorted in decreasing order of their bid price.
2. Sellers are sorted in increasing order of their ask price.
3. Auctioneer generates aggregate supply and demand curves
4. Auctioneer determines the number of participating buyers and sellers that satisfies (buyers willing to pay more than than sellers are asking for). 

A fundamental rule of any auction mechanim is that no participant can cheat once payment rules and allocations are established.

#### Payment Rules
We determine the price according to the competition among buyers and sellers. 
- Therefore the game reaches the SE (Stackelberg-Equation) 
- The strategy of hte auctioneer is a non-empty set within the range of min and max price. at some time t. THe maximum average social welfare for any gien x chosen by different prosumers. 


#### Real-Time DR Operation
1. Input
2. Output
3. Initial : ASWS
4. Determine both trading range price
5. For price p from max to min
6. Solve optimization problem
7. Auctioneer computes the average social welfare ASWS
8. Autioneer updates the optimal price and max average social welfare
9. Update price
10. Stackelberg equilibrium achieved

Stackelberg game between autcioneer and prosumer has a stackelberg game theoretic equilibrium.

Properties of the auction process
- the auction process can be considered a game in which there is always the possibility that participants will cheat (state a different amount of energy) when the auction process

#### Blockchain For Energy Trading
Overall Architecture :
Blockchain platform must meet certain criteria. It must be trustworthy, capable of fast computation for real-time energy trading algorithms, and must be able to store and retrieve data in a secure manner. It must also secure the privacy of the user. Prosumers must be paired in real-time, protect users private information and identifies the user to allow participation. Smart contracts are implemented as teh chain-code in the blockchain. 

Hyperledger Fabric : provides an immutable ledger and smart contract (chaincode) services to the blockchain platform. Transactions are generated as needed to execute smart contracts.The peer node in network executes the steps in the contract in sequence and the results are copied to the ledger. In hyperledger fabric, peers process transactions quickly because of the execute-order-validate process. 





#### Blockchain ? for Community?
Comparing a blockchain implementation to a non-blockchain implementation of the P2P energy trading system. A non-blockchain based system would use a central application hosted by a community manager. 


Maximizing the average social welfare is done by the auctioneer.


# Blockchain


# Case Studies?
- Blockchain technology on Electric Power Grids - A Case study in LO3 Energy
- 2021. 


DERs, ICT Infrastructure, and Blockchain
Label the emergence of this principle is changing the way society trades goods and services. 


Consumer-centric market views relies on P2P and community-based structures. Alternative market organization is generically named as aconsumer-centric electricity markets, while nerly 20 years ago this. 

P2P electricity trading empowers prosumers and consumers, leading to increased renewable energy deployment and flexibility in the grid. P2P platforms also aid in balancing and congestion management and providing ancillary services. The key enabling factors are distributed renewable energy resources, digitalization, and a conducive regulatory framework. Many pilots have been pioneered in Australia, Bangladesh, Colombia, Germany, Japan, Malaysia, the Netherlands, the UK, the US, and others have started trial peer-to-peer schemes. Many of the afore-mentioned pilot projects used blockchain technology.

Peer-to-peer electricity trading is a market-place where prosumers and consumers can trade electricity without an intermediary, at their agreed price. Trading based on P2P models makes renewable energy more accessible, empowers consumers, and allows them to make better use of their energy resources. 

IRENA project created a survey of innovations that are driving the creation of peer-to-peer energy markets in a 2019 report called, "Innovation Landscape for a renewable powered future". The synthesis report covers 30-key innovations identified acrossfour dimensions. 

|Enabling Technologies|Business Models|Market Design|System Operation|
|-|-|-|-|
| 1. Utility-Scale Batteries | 12. Aggregators|17. Increasing time granularity in electricity markets|25. Future role of distribution system ||operators|
|2. behind-the-meter batteries|13. Peer-to-peer electricity trading|18. Increasing space granularity in electricity markets|26. Co-operation ||between transmission and distribution system operators|
|3. Electric-Vehicle smart charging|14. Energy-as-a-service|19. Innovative ancillary services|27. Advanced forecasting of variable renewable ||power generation|
|4. Renewable power-to-heat|15. Community-ownership models|20. Re-designing capacity markets|28. Innovative operation of pumped hydropower ||storage|
|5. Renewable power-to-hydrogen|16. Pay-as-you-go models|21. Regional markets|29. Virtual power lines|
|6. Internet of Things||22. Time-of-use tariffs|30. Dynamic line rating|
|7. Artificial intelligence and big data||23. Market integration of distributed energy resources||
|8. Blockchain||24. Net billing schemes||
|9. Renewable mini-grids||||
|10. Supergrids||||
|11. Flexibility in conventional power plants||||

With P2P electricity trading, prosumers can share the benefits of generating electricity with the communities that they belong to, further encouraging the consumption and deployment of distributed renewable generation. The P2P business model can both contribute to power sector needs while also empowering consumers. 

Distributed energy resources are small or medium-sized resources, directly connected to the distribution network. They include distribution generation, energy storage (small-scale batteries), and controllable loads, such as electric vehicles, heat pumps, or demand response.


# Ongoing P2P Markt Initiatives

| P2P trading Platform | Country | Details
|-|-|-|
Brooklyn Microgrid | United States | Brooklyn Microgrid is a community energy market on a microgrid. Members can buy and sell energy from each other with smart contracts based on blockchain. (Mengelkamp et al., 2018)
Centrica plc | United Kingdom | Centrica is a pilot project to develop a local energy market in Cornwall, UK by testing the use of flexible demand, generation and storage, and rewarding consumers for bieng more fexible with their energy. Centrica is trialling the use of blockchain for this platform, using LO3's blockchain-powered energy trading platform (Centrica, 2018)
Lumenaza | Germany | Lumenaza's "utility-in-a-box" energy platform enables P2P energy sharing and communities on a local, regional and national level. The software connects producers of electricity with consumers, controls demand and supply and includes balance group management, aggregation, billing and visualization fo energy flows. It allows energy communities to particpate in electricity market design (Lumenaza, 2020). 
Piclo | United Kingdom | Piclo by open utility (a platform) and Good Energy ( a renewable energy power company) matches consumers and prosumers based on their preferences and locality, every 30 minutes. Custoemrs are provided with consumption data visualizations, and generators are provided with control and visibility over who buys power from them. Good Energy balances the peaks and valleys in generation, provides contracts and meter data, and does the billing (Piclo, 2019).
SOLshare | Bangladesh | SOLshare installs small-sscale mini-grids that connect local consumers and allow them to share electricity withn the locality. Consumers who have a solar panel installed on their homes can supply surplus power to others who do not have access to electricity. (UNFCC,2020)
sonnenCommunity | Germany | sonnenCommunity allows sharing of self-produced renewable power by individual consumers who are using sonnens batteries. This surplus energy is not fed into the grid, but into a virtual energy pool that supplies energy to other community members during times when they cannot produce. The price is fixed at USD 25 cents/kwh. The monthly usage fee for the platform is EUR 20 (sonnen, 2019).
Transactive Energy Initiative | Colombia | The pilot project activities include the development of a P2P trading app, the elaboration of policy recommendations for colombian policy makers and a roadmap for commercial scale-up (UCL, 2019).
Vendebron | Netherlands | Allows consumers to buy power directly from prosumers, at the price set by the prosumers. It behaves as an energy supplier that connects consumers. Provides suppliers with generation forecasting information for their assets. The monthly usage fee of the platform is USD 12 (Vanderbron, 2020)









## 1. Introduction

Distributed Energy Resources(DERs)
Electricity trading has changed in recent years with the advent of smart grid technologies. The increased availability of distributed generation with intelligent infrastructure has enabled residential consumers to harness energy and inject it into the distribution system. The consumers are now able to trade energy with each other and the grid. The new grid participants provides more decentralization to the smart grid. (Davis P,2014))The continuous integration of DERs, rooftop solar, energy storage, control devices and the advances in Information and Communication Technology (ICT) devices are transforming electricity consumers into prosumers.[[2]]




## References:
[1] Hien Thanh Doan, Joengho Cho, "Peer-to-Peer Energy Trading in Smart Grid Through Blockchain: A Double Auction-Based Game Theoretic Approach", in IEEE Access Journal, March 2021. DOI: 10.1109/ACCESS.2021.3068730

[2] Hien Thanh Doan, Joengho Cho, "Peer-to-Peer Energy Trading in Smart Grid Through Blockchain: A Double Auction-Based Game Theoretic Approach", in IEEE Access Journal, March 2021. DOI: 10.1109/ACCESS.2021.3068730

[3] Sakineh Khalili, Vahid Disfani, Mo Ahmadi, "Impact of Blockchain Technology on Electric Power Grids - A case study in LO3 Energy", ConnectSmart Research Laboratory, University of Tennessee at Chattanooga.(2020)





What is Peer-to-Peer Energy Trading


With the increasing connection of renewable energy sources, traditional energy consumers are becoming prosumers, who can both consume and generate energy [1]. The trends are extensive growth in small-scale distributed energy resources, which encompass behind-the-meter generation, energy storage, inverters, electric vehicles, and control loads [2]. The smart grid must grow to incorporate the bi-directional flow of electricity between supply and demand sources as penetration of Plug-in Electric Vehicles (PEVs) and distributed energy resources (DERs) like Photo-voltaic Solar Panels, (PV) increases in residential sectors. Peer-to-Peer (P2P) energy trading has emerged as a next-generation energy management mechanism for the smart grid that enables each prosumer of the network to participate in energy trading with other prosumers and the grid [3].  
Renewable energy sources are usually intermittent and difficult to predict. When prosumers have surplus electricity, they can curtail it, store it with energy storage devices, export it back to the power grid, or sell it to other energy consumers. The direct energy trading among consumers and prosumers is called peer-to-peer energy trading, which was developed based on the “P2P economy” concept (also known as sharing economy) [4] and is usually implemented within a local electricity distribution system.
With the prosumers in control of setting the terms of transactions and the delivering of goods and services [5], prosumers can gain more through trading with each other and the grid. [6] The challenge is that in a P2P network there isn’t a central authority that dictates the terms and settlement of transactions. A trustless system must be created that can simulate the needs and coordinate between competing agendas to reach a consensus for each participant while staying within the constraints of the physical systems. 
This paper aims to provide an overview of innovations around P2P energy trading networks:
-	We provide a background discussion on P2P networks, the features of trading, energy markets and an overview of the challenges in P2P trading.
-	We discuss the technical approaches adopted by current studies to devise various solutions in P2P trading.
-	We present potential research directions to investigate extensions of the current research practice
Elements of P2P Networks
The P2P energy trading markets have a virtual, and physical layer. The virtual layer essentially provides a secured connection for participants to decide on their energy trading parameters. It ensures that all participants have equal access to a virtual platform. The virtual platform facilitates the transfer of buy and sell orders, and financial transactions. The physical layer is a physical network that facilitates the transfer of electricity from sellers to buyers once the financial settlements between both parties are completed over the virtual layer platform. It can be a traditional distributed-grid network maintained by the independent system operator or an additional separate physical microgrid distribution grid, in conjunction with the traditional grid. [4]
Overview of Market Structure
Market operations of a P2P network consists of payment rules, and a clearly defined bidding format. The main objective is to enable an efficient energy trading process by matching the sell and buy orders in near real-time granularity. In market operations the generation of each producer influences the thresholds of maximum and minimum energy allocation. Different market-time horizons may exist in the market operation that should be able to produce enough allocation at every stage of operation. [2] Fully decentralized markets allow for prosumers to independently and directly negotiate with each other to decide on energy trading parameters without any centralized supervision by leveraging bilateral contracts between prosumers. In a fully decentralized market the bilateral contracts capture both the upstream-downstream energy balance as well as forward market uncertainty. [8] Community-based market can be applied to community microgrids and group of neighboring prosumers. The members of the community share common interests and goals even though they are not at the same location. [9] may work either in a collaborative or competitive manner. [10] Participants generally trade energy through a community manager. The community manager manages exchanges outside of the community. Privacy is preserved by the community manager. [9] Composite market combines the fully decentralized and community-based market designs. An individual prosumer can engage in P2P trading between each other, while also interacting with existing markets like fully distributed markets. [11] Community manager can also oversee trading inside the community. [12]
Overview of Existing Challenges
The challenges for the physical layer of P2P is the integration of sensors and smart power systems that can support flexible loads and dynamic generation. The penetration of DERs and energy storage currently provide insignificant shifts in the overall grid operation but will soon grow into more substantial impacts if trends in technology persist. [] The virtual layer for P2P trading hinges on the information system that communicates the transactions between physical layer and in-between participants.
The P2P Information system needs to be able to:
1.	enable all market participants to communicate with one another for participating in energy trading;
2.	integrate the participants within a suitable market platform;
3.	give the participants equal access to the market;
4.	monitor the market operation;
5.	set restrictions on participant's decisions to ensure network security and reliability.
Game-theory for P2P trading

Using Game-Theory in P2P
Game and auction-theoretic models have been used in P2P energy trading as an effective means of energy management approaches. The development of P2P energy trading has the potential to substantially benefit prosumers in terms of earning revenues, reducing electricity costs, and lowering their dependency on the grid. Custom Papers/References > Designing microgrid energy markets - A case study The Brooklyn Microgrid
The system poses the challenge of modeling the decision-making process of each participant for the greater benefit of the entire energy network while considering human factors, e.g., rationality, motivation, and environmental friendliness. Particularly, in settings where there are many users with conflicting interests participating, it would be challenging either to integrate such conflicting interests when designing the decision-making process of each participant or, if necessary, to motivate the users to cooperate with reducing costs, maximizing revenues, and pursuing renewable energy objectives. [4] 
An energy management solution is needed that provides efficient and robust operation considering the conflicting nature of energy trading. Game theory should be a very effective tool for modeling the decision-making process of participants.
Basic Game-Theoretic Concepts
Game theory is a mathematical and signal processing tool that analyzes Custom Papers/References > Economics of electric vehicle charging A game theoretic approach strategies in competitive solutions where the outcome of a participants choice is based on the actions of other participants. There are two main branches: 1. noncooperative and 2. cooperative game theory.
Non-Cooperative games
These types of games allow players to take necessary action, to make optimal decisions, without any coordination or communication with each other. Noncooperative games can be further divided into 'static' or 'dynamic' games.
•	Static game: Players act only once, either simultaneously or at different times. An example could be two business owners deciding where to open a new store location.
•	Dynamic game: Players act more than once and have input regarding the choices of other players. Time can play a central role in these games. Dynamic games can be modeled as a series of static games, but time and information would need to be reflected in the utility functions. An example of a dynamic game would be Chess.
For both types of non-cooperative games, the players will make decisions based on "pure strategy" a deterministic way, or a probabilistic way "mixed strategy".[4] The most popular concept in non-cooperative games is the solution concept called the Nash equilibrium. It refers to a stable state of a non-cooperative game where neither player can improve its utility by unilaterally altering its action when other players actions are fixed. An example in the game of Monopoly is when there are no more actions the player can make with the money on hand that could better the situation. A Nash equilibrium always exists in a game with mixed strategies (probabilistic decisions) but not always guaranteed in pure strategies (deterministic). Finally the non-cooperative game may have multiple Nash equilibriums and the most desirable one should be chosen for the solution. Custom Papers/References > Noncooperative and cooperative optimization of electric vehicle charging under demand uncertainty A robust stackelberg game
Cooperative games
•	Canonical Coalitional game:
•	Coalition Formation game:
•	Coalition Graph game:
Game-Theoretic Applications for P2P
The application of game theory in energy trading and management is extensive. However, the discussion of its application in the field of P2P energy trading is limited, which could be because of the relatively recent emergence and exploration of P2P trading frameworks in energy domains [4].
Coalitional Energy Trading
If small scale electricity suppliers and consumers are participants on the network and are connected on the physical layer through local distribution that can be islanded off, then there is potential for trading energy in an isolated fashion. The discrepancy between the wholesale price and retail price matters because the peer-to-peer trading price will be greater than the wholesale price but less than the retail price. The consumers will always want to trade with a peer because it would be cheaper than retail energy traveling over long transmission lines. The local prosumers would also benefit from the trading price being more than the wholesale price of creating the electricity and therefore gaining profit. Custom Papers/References > Direct electricity trading in smart grid A coalitional game analysis
The coalition formed between prosumers is a canonical coalitional game with transferable utility, and the price for P2P energy trading is determined by an asymptomatic Shapley value Custom Papers/References > Coalitional game theory for communication networks. The net surplus of the coalition is sold to the retail market at wholesale prices but bought at retail prices if there is a net deficiency. The coalition can then effectively ban together to optimize the return on energy generated and consumed by trading with each other before selling or purchasing from the grid.
There are only 10 states that still pay the wholesale price (avoided cost) when selling back to the grid. All other states pay retail price to sell to the grid. In these states the super additivity of the grand coalition is no longer viable and there is no reason to stay in the coalition. Custom Papers/References > Net Metering is a Win-Win for Utilities and Local Communities An avoided cost (also known as net-metering) is the minimum amount an electric utility is required to pay an independent power producer, under the PURPA regulations of 1978, equal to the costs the utility calculates it avoids in not having to produce that power (usually substantially less than the retail price charged by the utility for power it sells to customers).
Day-Ahead Optimization
With a view toward reducing the cost of energy trading within the grid, a day-ahead optimization process regulated by an independent central unit has been proposed in Custom Papers/References > Demand-side management via distributed energy generation and storage optimization. The existence of optimal strategies is proven, and, furthermore, the authors present a distributed algorithm to be run on the users’ smart meters, which provides optimal energy-production and storage strategies while preserving user privacy and minimizing required central unit communication.
Auction Games for DERs
Auction games have been proposed for trading both storage space and renewable energy from DERs [10] The real-time implementation of a multiagent-based game-theoretic reverse auction model for microgrid market operations featuring conventional and renewable DERs is discussed. Custom Papers/References > Real-time implementation of multiagent-based game theory reverse auction model for microgrid market operation The proposed methodology was realistically implemented in a smart grid system at Florida International University, and the subsequent investigation shows that the proposed algorithm and the industrial hardware-based infrastructure are suitable for implementation in the existing electric utility grid.
Meanwhile, the authors in [10] utilize an auction game to study the solution of joint-energy-storage ownership sharing between multiple shared facility controllers (SFCs) and those dwelling in a residential community. The auction process possesses both incentive-compatibility and individual-rationality properties and is also capable of enabling the residential units (RUs) to decide the fraction of their shared energy storage capacity with the SFCs of the community to assist in storing electricity
For example, in Custom Papers/References > Direct electricity trading in smart grid A coalitional game analysis a coalitional game is used to study the cooperation between small-scale DERs and energy users to enable the direct trading of energy without going through retailers. The asymptotic Shapley value is the core of the coalitional game so that no small-scale DERs or energy users have an incentive to abandon the coalition, which suggests the stable direct trading of energy for the proposed pricing scheme. Furthermore, numerous case studies demonstrate that the scheme is suitable for practical implementation. The authors in [9] focus on comprehensive economic power transactions of multiple microgrid networks with multiple agents; they design a three-stage algorithm based on a coalitional game strategy and include request, exchange, merge-and-split, and cooperative transaction stages. The developed algorithm enables microgrids to form coalitions where each microgrid can exchange power directly by paying a transmission fee.
Blockchain for P2P
When communicating between many participants an encrypted form of communication can be used to secure transactions between the participants. They all work towards processing the message and providing a consensus on what the message between any two participants should be. This consensus across all participants is crucial for trustless systems. In P2P networks a blockchain messaging mechanism can be used to validate financial transactions on a distributed ledger, it can also be used to track energy usage without the fear of tampering with the metering information over the air. The attack would need to achieve 51% control of the network in order to approve the false transactions. In an unsecure network the attack would only need to override a single node and create false readings for a meter or a financial transaction. In a federated system the operator would oversee securing the infrastructure and communications. But in an open P2P network design cryptographic methods such as blockchain provide unfederated security, privacy and protection against the network.
Conclusion
pending
Discussion of Future Research Direction
•	Network Charge Identification
•	Large Scale Network trading and simulation
•	Benefit to the grid
•	Ancillary Service to the grid (virtual power plants)
•	Multi-level storage management
•	Prioritizing stakeholders
•	Injection limit and market mechanism
•	Unified model
•	Enabling data accessibility with privacy (using the anonymous gaming algorithms to hide information on the energy trading platform?)
•	Inter and Intra-community trading

References

1.	Luo Y, Davis P. Autonomous Cooperative Energy Trading Between Prosumers for Microgrid Systems. 3rd IEEE International Workshop on Global Trends in Smart Cities go SMART; 2014. 
2.	Wayes Tushar, Senior Member, IEEE,Tapan K. Saha,Fellow, IEEE,Chau Yuen,Senior Member, IEEE, David Smith, Member, IEEE, and H. Vincent Poor, Fellow, IEEE, “Peer-to-Peer Trading in Electricity Networks: An Overview”, arXiv:2001.06882v1 [cs.MA] 19 Jan 2020
3.	W. Tushar, C. Yuen, H. Mohsenian-Rad, T. Saha, H. V. Poor, and K. L. Wood, “Transforming energy networks via peer-to-peer energy trading: The potential of game-theoretic approaches,” IEEE Signal Processing Magazine, vol. 35, no. 4, pp. 90–111, July 2018.
4.	Hamari, Juho; Sjöklint, Mimmi; Ukkonen, Antti (2016). "The Sharing Economy: Why People Participate in Collaborative Consumption". Journal of the Association for Information Science and Technology. 67 (9): 2047–2059. doi:10.1002/asi.23552
5.	T. Morstyn, N. Farrell, S. J. Darby, and M. D. Mcculloch, “Using peer-to-peer energy-trading platforms to incentivize prosumers to form federated power plants,” Nature Energy, vol. 3, no. 2, pp. 94–101, 2018. 
6.	W. Tushar, T. K. Saha, C. Yuen, T. Morstyn, M. D. McCulloch, H. V. Poor, and K. L. Wood, “A motivational game-theoretic approach for peer-to-peer energy trading in the smart grid,” Applied Energy, vol. 243, pp. 10–20, June 2019.
7.	W. Tushar, T. K. Saha, C. Yuen, P. Liddell, R. Bean, and H. V. Poor, “Peer-to-peer energy trading with sustainable user participation: A game theoretic approach,” IEEE Access, vol. 6, pp. 62 932–62 943, Oct. 2018.
8.	T. Morstyn, A. Teytelboym, and M. D. Mcculloch, “Bilateral contract networks for peer-to-peer energy trading,” IEEE Transactions on Smart Grid, vol. 10, no. 2, pp. 2026–2035, Mar. 2019.
9.	J. Ni and Q. Ai, “Economic power transaction using coalitional game strategy in micro-grids,” IET Generation, Transmission Distribution, vol. 10, no. 1, pp. 10–18, Jan. 2016.
EIA, "Subsequent Events -California’s Energy Crisis,". 
10.	W. Tushar, B. Chai, C. Yuen, S. Huang, D. B. Smith, H. V. Poor, and Z. Yang, “Energy storage sharing in smart grid: A modified auction-based approach,” IEEE Trans. Smart Grid, vol. 7, no. 3, pp. 1462–1475, May 2016.
11.	N. Liu, X. Yu, W. Fan, C. Hu, T. Rui, Q. Chen, and J. Zhang, “Online energy sharing for nano grid clusters: A Lyapunov optimization approach,” IEEE Transactions on Smart Grid, vol. 9, no. 5, pp. 4624–4636, Sept. 2018. 
12.	L. W. Park, S. Lee, and H. Chang, “A sustainable home energy prosumer chain methodology with energy tags over the blockchain,” MDPI Sustainability, vol. 10, no. 3, pp. 658:1–658:18, Feb. 2018.
13.	T. Sousa, T. Soares, P. Pinson, F. Moret, T. Baroche, and E. Sorin, “Peer-to-peer and community-based markets: A comprehensive review,” Renewable and Sustainable Energy Reviews, vol. 104, pp. 367–378, Apr. 2019.
14.	W. Tushar, W. Saad, H. V. Poor, and D. B. Smith, “Economics of electric vehicle charging: A game theoretic approach,” IEEE Trans. Smart Grid, vol. 3, no. 4, pp. 1767–1778, Dec. 2012.
15.	Liang-Cheng, J. F. D. Rodrigues, and H. X. Lin, “Analysis of feed-in tariff policies for solar photovoltaic in China 2011-2016,” Applied Energy, vol. 203, pp. 496–505, Oct. 2017.
16.	M. E. Peck and D. Wagman, “Energy trading for fun and profit buy your neighbor’s rooftop solar power or sell your own-it’ll all be on a blockchain,” IEEE Spectrum, vol. 54, no. 10, pp. 56–61, Oct. 2017.
17.	W. Tushar, B. Chai, C. Yuen, D. B. Smith, K. L. Wood, Z. Yang, and H. V. Poor, “Three-party energy management with distributed energy resources in smart grid,” IEEE Transactions on Industrial Electronics, vol. 62, no. 4, pp. 2487–2498, Apr. 2015.
18.	W. Tushar, T. K. Saha, C. Yuen, T. Morstyn, N.-A. Masood, H. V. Poor, and R. Bean, “Grid influenced peer-to-peer energy trading,” IEEE Transactions on Smart Grid, 2019, early Access. 
19.	C. Zhang, J. Wu, Y. Zhou, M. Cheng, and C. Long, “Peer-to-Peer energy trading in a Microgrid,” Applied Energy, vol. 220, pp. 1–12, June 2018. 
20.	E. Mengelkamp, J. G¨arttner, K. Rock, S. Kessler, L. Orsini, and C. Weinhardt, “Designing microgrid energy markets - A case study: The Brooklyn Microgrid,” Applied Energy, vol. 210, pp. 870–880, Jan. 2018. 
21.	M. Andoni, V. Robu, D. Flynn, S. Abram, D. Geach, D. Jenkins, P. McCallum, and A. Peacock, “Blockchain technology in the energy sector: A systematic review of challenges and opportunities,” Renewable and Sustainable Energy Reviews, vol. 100, pp. 143–174, Feb. 2019.
22.	J. Guerrero, A. C. Chapman, and G. Verbiˇc, “Decentralized P2P energy trading under network constraints in a low-voltage network,” IEEE Transactions on Smart Grid, 2018, early
23.	T. Baroche, P. Pinson, R. L. G. Latimier, and H. B. Ahmed, “Exogenous cost allocation in peer-to-peer electricity markets,” IEEE Transactions on Power Systems, vol. 34, no. 4, pp. 2553–2564, July 2019.
24.	W. Hou, L. Guo, and Z. Ning, “Local electricity storage for block chain-based energy trading in industrial Internet of Things,” IEEE Transactions on Industrial Informatics, vol. 15, no. 6, pp. 3610–3619, June 2019.
25.	Z. Li, J. Kang, R. Yu, D. Ye, Q. Deng, and Y. Zhang, “Consortium blockchain for secure energy trading in industrial internet of things,” IEEE Transactions on Industrial Informatics, vol. 14, no. 8, pp. 3690–3700, Aug. 2018.
26.	O. Jogunola, A. Ikpehai, K. Anoh, B. Adebisi, M. Hammoudeh, H. Gacanin, and G. Harris, “Comparative analysis of P2P architecture for energy trading and sharing,” Energies, vol. 11, no. 1, pp. 62:1–62:20, Dec. 2018.
27.	E. Sorin, L. Bobo, and P. Pinson, “Consensus-based approach to peer-topeer electricity markets with product differentiation,” IEEE Transactions on Power Systems, vol. 34, no. 2, pp. 994–1004, Mar. 2019
28.	C. Wu, H. Mohsenian-Rad, and J. Huang, “Vehicle-to-aggregator interaction game,” IEEE Trans. Smart Grid, vol. 3, no. 1, pp. 434–442, Mar. 2012.
29.	H. K. Nguyen and J. B. Song, “Optimal charging and discharging for multiple PHEVs with demand side management in vehicle-to-building,” J. Commun. Netw., vol. 14, no. 6, pp. 662–671, Dec. 2012.
30.	Paudel, K. Chaudhari, C. Long, and H. B. Gooi, “Peer-to-peer energy trading in a prosumer-based community microgrid: A game-theoretic model,” IEEE Transactions on Industrial Electronics, vol. 66, no. 8, pp. 6087–6097, Aug. 2019. 
31.	P. Baez-Gonzalez, E. Rodriguez-Diaz, J. C. Vasquez, and J. M. Guerrero, “Peer-to-peer energy market for community microgrids [technology leaders],” IEEE Electrification Magazine, vol. 6, no. 4, pp. 102–107, Dec. 2018.
32.	Chenghua Zhang, "Peer-to-Peer Energy Trading in Electrical Distribution Networks," Cardiff University, PHD Thesis, 2017.
33.	L. D. Xu, W. He, and S. Li, “Internet of Things in industries: A survey,” IEEE Trans. Ind. Inform., vol. 10, no. 4, pp. 2233–2243, Nov. 2014. 
34.	B.W.F. Depoorter, “Regulation of Natural Monopoly,” Encycl. Law Econ., (published).
35.	S. Hunt, Making competition work in electricity.Ch.2 p.27 John Wiley & Sons, New York, 2002. 
36.	W. Troesken, “Regime Change and Corruption. A History of Public Utility Regulation”; pp. 259-82 in Corruption and Reform: Lessons from America's Economic History, Edited by E. L. Glaeser, C. Goldin. University of Chicago Press, United States, 2006. 
37.	Public Utility Holding Company Act of 1935. United States, 1935.
38.	Public Utility Regulatory Policies Act of 1978. 1980. 
39.	M.W. White, “Power Struggles: Explaining Deregulatory Reforms in Electricity Markets,” Brookings Pap. Econ. Act. Microeconomics, 201–267 (1996). doi:10.2307/2534749. 
40.	K. Mcdermott," Cost of Service Regulation In the Investor-Owned Electric Utility Industry A History of Adaptation," Edison Electric Institute, Washington, DC, June 2012. 
41.	L. Cabral, “The California Energy Crisis,” Japan World Econ., 14 [3] 335–339 (2002). 
42.	P. Joskow and E. Kahn, “A quantitative analysis of pricing behavior in California’s wholesale electricity market during summer 2000,” Spec. Publ. IEEE Power. Soc., 1 392–394 (2001). 
43.	C. Weare, The California Electricity Crisis: Causes and Policy Options. Ch. 3 pp. 1- 119. Public Policy Institute of California, USA, 2003
44.	Spandana Vottem, B.S. "APPLICATION OF COOPERATIVE GAME THEORY IN SMART GRIDS", A thesis submitted to the Graduate Council of Texas State University in partial fulfillment of the requirements for the degree of Master of Science with a Major in Engineering December 2019.
45.	C. Hicks, "The smart grid - where are we today and what the future holds," ERB Institute, University of Michigan, Michigan 2012.
46.	Naser Hossein Motlagh, Mahsa Mohammadrezaei and Julian Hunt and Behnam Zakeri, "Internet of Things (IoT) and the Energy Sector" Department of Computer Science, University of Helsinki, FI-00560 Helsinki, Finland; Energies 2020.
47.	Nizam, M.; Wicaksono, F.X.R. Design and Optimization of Solar, Wind, and Distributed Energy Resource (DER) Hybrid Power Plant for Electric Vehicle (EV) Charging Station in Rural Area. In Proceedings of the 2018 5th International Conference on Electric Vehicular Technology (ICEVT), Surakarta, Indonesia, 30–31 October 2018.
48.	X. Fang, S. Member, S. Misra, and G. Xue, “Smart Grid – The New and Improved Power Grid: A Survey,” IEEE Commun. Surv. Tutorials, 14 [4] 944–980 (2011).
49.	National Academies of Sciences, Engineering, and Medicine. “The Power of Change: Innovation for Development and Deployment of Increasingly Clean Electric Power Technologies”, The National Academies Press, Washington D.C., 2016.
50.	Hamari, Juho; Sjöklint, Mimmi; Ukkonen, Antti (2016). "The Sharing Economy: Why People Participate in Collaborative Consumption". Journal of the Association for Information Science and Technology. 67 (9): 2047–2059. doi:10.1002/asi.23552.
51.	Internet of Things-aided Smart Grid: Technologies, Architectures, Applications, Prototypes, and Future Research Directions Yasir Saleem, Student Member, IEEE, Noel Crespi, Senior Member, IEEE, Mubashir Husain Rehmani, Senior Member, IEEE, and Rebecca Copeland
52.	Jing Zhang,Ruiming Yuan, Zhenyu Jiang,He Yin, "Consensus Network Based Distributed Energy Management for PV-Based Charging Station", IEEE 2017.
53.	"Net Metering is a Win-Win for Utilities and Local Communities" (https://web.archive.org/web/20131001171510/http://www.cres-energy.org/blogs/blogs_newton_07apr.html). _Cres-energy.org_. Archived from [the original](http://www.cres-energy.org/blogs/blogs_newton_07apr.html)on 2013-10-01. Retrieved 2013-12-15.
54.	H. Yang, X. Xie, and A. V. Vasilakos, “Noncooperative and cooperative optimization of electric vehicle charging under demand uncertainty: A robust Stackelberg game,” IEEE Trans. Veh. Technol., vol. 65, no. 3, pp. 1043–1058, Mar. 2016.
55.	W. Saad, Z. Han, M. Debbah, A. Hjørungnes, and T. Basar, “Coalitional game theory for communication networks,” IEEE Signal Process. Mag., vol. 26, no. 5, pp. 77–97, Sept. 2009.
56.	Atzeni, L. G. Ordòñez, G. Scutari, D. P. Palomar, and J. R. Fonollosa, “Demand-side management via distributed energy generation and storage optimization,” IEEE Trans. Smart Grid, vol. 4, no. 2, pp. 866–876, June 2013. 
57.	M. H. Cintuglu, H. Martin, and O. A. Mohammed, “Real-time implementation of multiagent-based game theory reverse auction model for microgrid market operation,” IEEE Trans. Smart Grid, vol. 6, no. 2, pp. 1064–1072, Mar. 2015
58.	W. Lee, L. Xiang, R. Schober, and V. W. S. Wong, “Direct electricity trading in smart grid: A coalitional game analysis,” IEEE J. Sel. Areas Commun., vol. 32, no. 7, pp. 1398–1411, July 2014.
59.	"What Can Be Learned from California’s Electricity Crisis?" Public Policy Institute of California, San Francisco, Jan 2003.
60.	Jing Zhang, “Consensus Network Based Distributed Energy Management for PV-Based Charging Station”  
61.	M A Hannana, Z A Ghania, A Mohameda and M. N. Uddin, Real-Time Testing of a Fuzzy Logic Controller Based Grid-Connected Photovoltaic Inverter System, Department of Electrical, Electronic & Systems Engineering Universiti Kebangsaan Malaysia, 43600 Bangi, Selangor, Malaysia Department of Electrical Engineering, Lakehead University Thunder Bay, Ontario P7B 5E1, Canada hannan@eng.ukm.my
62.	Pablo García-Triviño, Decentralized Fuzzy Logic Control of Microgrid for Electric Vehicle Charging Station Pablo García-Triviño, Juan P. Torreglosa, Luis M. Fernández-Ramírez, Senior Member, IEEE, and Francisco Jurado,Senior Member, IEEE
63.	H. Yin, C. Zhao, M. Li, C. Ma, and M. Y. Chow, “A game theory approach to energy management of an engine genera-tor/battery/ultracapacitor hybrid energy system,” IEEE Transactions on Industrial Electronics, vol. 63, no. 7, pp. 4266–4277, 2016.
64.	W. Tushar, W. Saad, H. Poor, and D. Smith, “Economics of electric vehicle charging: A game theoretic approach,”IEEE Trans. Smart Grid
65.	A. Kulkarni and U. V. Shanbhag, “On the variational equilibrium as a refinement of the generalized Nash equilibrium,”Automatica, vol. 48,no. 1, pp. 45–55, 2012
66.	Energy Policy Act of 1992. Unites States,1992. 
67.	Energy Information Administration, "The changing structure of the electric power industry: Selected issues," Rept. DOE/EIA-0562, Department of Energy, Washington, DC, July 1998. 
68.	Navigant Consulting Inc, "Evolution of the Electric Industry Structure in the U.S. and Resulting Issues," Navigant Consulting Inc, Washington, DC, October 2013. 
69.	K. Mcdermott," Cost of Service Regulation In the Investor-Owned Electric Utility Industry A History of Adaptation," Edison Electric Institute, Washington, DC, June 2012. 
70.	S. Borenstein and J.B. Bushnell, "The U.S. Electricity Industry after 20 Years of Restructuring,"Energy Institute at HAAS, May 2015. 
71.	H. Demsetz, “Why Regulate Utilities?” J. Law Econ., 11 [1] 55-65 (1968).
72.	R.R. Geddes, “A Historical Perspective on Electric Utility Regulation,” CATO Rev. Bus. Gov., Winter 75–82 (1992). 
73.	G.A. Jarrell, “The Demand for State Regulation of the Electric Utility Industry,” J. Law Econ., 21 [2] 269–295 (1978). 
74.	H. Averch and L. Johnson, “Behavior of the firm under regulatory constraint,” Am. Econ. Rev., 52 [5] 1052–1069 (1962). 
75.	Clean Air Amendments of 1970. United States, 1970. 
76.	"Total electricity end use in the U.S. from 1975 to 2014 (in billion kilowatt hours)" (2014) In Statista.

77.	SAEED AZAD, "A GAME THEORETIC APPROACH TO A RETAIL ELECTRICITY MARKET WITH A HIGH PENETRATION OF SMALL AND MID-SIZE RENEWABLE SUPPLIERS",ALFRED UNIVERSITY,ALFRED, NEW YORK APRIL, 2016
78.	Liu, F.Richard Yu "Performance Optimization for Blockchain-Enabled Industrial Internetof Things (IIoT) Systems: A DeepReinforcement Learning Approach", IEEE TRANSACTIONS ON INDUSTRIAL INFORMATICS, VOL. 15, NO. 6, JUNE 2019
79.	[6], [30], [39], [43], [24], [46], [47], [10], [49], [27], [83], [64], [82], [40], [84], [3]

