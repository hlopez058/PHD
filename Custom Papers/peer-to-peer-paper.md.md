# Peer-To-Peer Energy Trading



## 1. Introduction
In recent years, there has been an urgent pursuit of an alternative energy system in which energy production, transmission, distribution, and consumption can take place in an environmentally sustainable fashion. As a result, the development of smart, sustainable, and green solutions is becoming more significant, including the widespread deployment of distributed energy resources (DERs) at residences [1], the introduction of electric vehicles (EVs) [2], and the establishment of various smart energy services, e.g., demand response management [3], for the effective management of energy resources within the electricity grid. Consequently, different signal processing techniques, e.g., machine learning, artificial intelligence (AI) [4], and game theory [5], have been offered as solutions to consumers.

## 2. Network Elements of P2P Trading 

- Distributed Network architecture

- Virtual and physical layers
(Create a diagram to show virtual and physical layers)

Elements in the virtual layer:
- Information system
- Market operation
- Pricing mechanism
- Energy mangement

Elements in the physical layer
- Grid connection
- Metering
- Communication infrastructure

Other Elements
- Market participants
- Regulation

Market Structure P2P Trading
- Fully decentralize market
- Community based market
- Composit market

P2P Trading  Exisiting Challenges
- P2P Trading Challenges Virtual Layer
	- Reducing Cost energy
	- Balancing local generation and demand
	- Incentivizing & engaging prosumers
	- Developing pricing mechanism
	- Identifying uncertainty and asynchronicity
	- Securing transactions
- P2P tradin challenges in physical layer
	- violation of voltage & capacity constraints
	- increase in network power loss
	- loss of system strength

P2P Trading : overview  technical
- Game Theory
	- Preliminary 
	- Non-coopertive 
	- Cooperative game
- Cannonical coalition game
- Coalition formation game
- Coalition graph game 
- Game theory for P2P trading in the virtual layer
- Game theory for P2P trading in the physical layer

Double Auction
- Preliminary , a step-by-step process in , [90],[91]
	- sellers submit the reservation prices in an increasing order
	- buyers are arranged in a decreasing order of thier reservation bids.
	- once the sellers and buyers orders ar ordered the aggregated supply and demand curves are generated that meet at a intersection point. 
	- the intersection point establishes the auction price and the number of sller and buyers that eventually engage in the market trading process. 
- Double Auction for P2P trading in the virtual layer: Double auction technique has been used by [25][51][82][57], to achieve objectives of balancing local generation and demand , shaping ht edemand at the peak hour. 
- Double auction for P2P trading in the physica layer: [14] proposes a decentralize layer, 

- Double theproperly creating . 








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
