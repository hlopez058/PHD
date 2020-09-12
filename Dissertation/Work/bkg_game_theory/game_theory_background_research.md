\documentclass{article}
# Theoretical Background and Literature Review

Hector Lopez - Florida Atlantic University

Revision 1.0 8/20/2020

## Introduction to Game theory

According to [1] Game theory is a mathematical tool and conceptual framework that 
can be used to study complex, self-interested interactions among rational players. 
A simpler explanation is that Game theory is the science of decision making. It originated in the minds of great economists like Von Nuemann and Morgeston as early as 
the 1940's as a way to explain the behaviour economics. It was then further developed
to be used in financial markets. The theory really thrived in the 1950's when John Nash published several works around non-cooperative Games that where applied more broadly. 
Unfortunately in later years the discovery that a well-defined value system must be first defined before expecting the solutions dervied through Game theory to actually be accurate. The varying nature of human value systems prevented significant in-roads in areas where human players where considered, but it did not stop the application to various fields with defined constraints such as control-loops, war-fare, ecology, etc..[1]

There are many definitions for what a *game* is in Game theory, but lets 
consider the definition proposed by [2] where they state that a game is any situation 
involving more than one individual, each of which can make more than one 
action, such that the outcome to each individual, called the *payoff*, 
is influenced by their own action, and the choice of action of at least one other individual. In other words a situation where rational agents take actions according to 
a strategy to maximize their own utility. Many situations can be arranged in 
this way to solve complex systems involving many decisions. [2]

A way to think of what is meant by *strategy* in Game theory lets consider the analogy proposed by [19] by imagining you where playing a game of chess. The caveot is that you are playing via a representative, so in order to play the game you must create a set of instructions for every possible circumstance that may arise during the game. That means for the first move they make you must design outline the response for every reaction of the opponents move. The entire set of these decisions all the way until the end-game is a strategy for the player. A deterministic game like chess can be mapped out this way (even if it would be a very tedious excercise). These types of games are called finite because tehre are a limited number of moves. They are also considered a zero-sum game because one players gain equals the other players loss. Also, this game can be considered a compettitive game or a *Non-cooperative* game because both players are competing to increase their own utility at the expense of the other. 

Game theory can be categorised into three main branches: *Non-Cooperative* game theory, as mentioned above, *Cooperative* game theory (coalitional game theory) and relatively recent branch called *Evolutionary* game theory (EGT). The contributions to game theory can be found in Figure 1. as presented in [3], it shows cooperative game theory was founded by Neumann and Morgenstern [10], and then non-cooperative game was represented by Nash’s work [11],[12],[13],[14]. 

John Nash proved the existence of non-cooperative game solution, that is,the existence of Nash equilibrium (further explained later), thus laying the theoretical foundation of the modern non-cooperative game. Non-cooperative game theory essentially studies the settings where multiple payoff-maximising players, who have partially or totally contradictory interests over the system and/or personal outcomes, interact with each other. 

Cooperative games are based on the Shaply value, a value that calculates the *fair* payoff of a player in a coalition of players. In a cooperative game all players are aware of the strategies chosen by other players. The goal in a cooperative game is to maximize the reward of all players involved. An example would be a group of homes with energy storage capacity and roof-top solar power generation working together to maximize overall revenue by selling energy at peak demand and meeting dynamic loads between them. 

![timeline of GT](./img/timeline_gt.png "Figure 1" =300x)
*Fig. 1. History of Game Theory .*


![class of GT](./img/game_classification.png "Figure 2" =300x)
*Fig. 1. Game classification .*

  On the contrary, cooperative game theory could be applied to situationswhere communication among players is enabled, and the fundamental modelling unit incooperative game theory is the set of players.[1]

As for the evolutionary game, it is generally recognized that it was officially founded by Maynard Smith and Price [15]. This theory can be regarded as an organic combination of general game theory and dynamic evolution process [16]. Among these, the former focuses on the game problem within the framework of *bounded rationality* rather than *complete rationality*, while the latter draws on the biological evolution theory in biology field. In short, the decision-making stakeholders (i.e., playersor participants) in an evolutionary game constantly adjust their own strategies according to environmental changes and the strategies of other decision-making stakeholders in orderto adapt to the game environment under the conditions of limited knowledge, information and reasoning ability [9], [17].

### Standard Game Model

#### Basic Elements

A standard game model is a situation when there is more than one intelligent and purposeful agent and it includes at least 4 major elements [2],[9],[4]:

1) Players/Participants :  The  participants  in  the  game  who  can  decide  their  own  strategies.  An  important  assumption  is  that  the  players are rational, which means that they don’t leave things to chance and don’t take advantage of others’ mistakes. If we assume rational agents that have all rationality and all relevant information then the agent can model the game as an optimization problem. Unfortunately people do not always choose the most rational choice in real life. This then reduces the accuracy of classical game theory. Optimization is not just a single value system but many that also optmizes accross social and cultural systems.[1]

2) Strategy : A collection of all the strategies available for all players. According to whether a player’s strategies are finite, we can divide games into three groups: *finite games* and *infinite games*. Sometimes a strategy set can be infinite since it can by almost any option, or only 3 for example in the game of rock, papers, scissors. There are some strategies that do not involve randomness (finite strategy) such as to tic-tac-toe.finite games are also known as *matrix  games*. An  *infinite  game*  is  said  to  be  a *continuous-kernel*  game if  the  action  sets  of the players are continua, and the players’ objective functions are continuous with respect to action variables of all players.[5]

3) Pay-offs/Payment: After each player in the game chooses a  strategy  from  their  own  strategies  set,  a  relevant  result  (a  group of data) is provided to show each player’s gain or loss. A good payoff is the fundamental goal of a player, and is the main basis of a player’s judgment and behavior. Pay-offs are also known as the players preferences described as 'utility' and must be understood clearly for the model to be effective. The payoffs are very subjective. If there is a ranking to the payoff it is called *ordinal* , if it is just a subjective quantity value then it is a *cardinal* payoff.[1]

4) Orders:  When  different  players  are  about  to  decide,  there is a need to decide the orders. Sometimes players make their decisions at the same time to make sure that the game is fair;  sometimes  players  make  decisions  one  after  another;  most times in reality players may choose their strategies more than once.  Different orders result in quite different situations.

#### Common Models

In an *n*-player game, the goal of the participants is usually to minimize payments or maximize incomes. Based on this, a typical *n*-player game [9] can be expressed as

$$G = [N;S_{1},S_{2},...,S_{n};u_{1},u_{2},...,u_{n}]$$ (1)

Where the game is *G*, and *N* represents a set of players in the *n*-player game. The *S* series represents the strategies of each *n*-player. Finally the *u* represents the payment for each *n*-player. 

The normal-form representation for the standard game model is the pay-off matrix as described by [2]. Each column and row represents the associated payoffs for each strategy as a combination of the two players. Given a strategy 'A' and a strategy 'B' a matrix of the game can be drawn to represent the responses of Player1's (P1) decision of strategy A and B while Player 2 (P2) chooses either A or B. The value at each cell then represents the reward/loss of the decision for each player.

|P1 \ P2|  |     |
|:--:|:---:|:---:|
|   | A   | B   |
| A | 1,1 | 0,0 |
| B | 0,0 | 2,2 |


## Types of Games

### Cooperative

Cooperative games in game theory are focused on the generic strategy of the game to provide a fairness result for each participant.[5] Since cooperative games are mainly supported by some contractual agreement the idea is tha the agents in the game are acting out of the desire to make the rewards as fair as possible. The complications arise with the decisions of what contributions should result in wieghing the rewards and how parts of the game can have different rewards and thus different weights attributed to make the reward system as balanced and fair as possible. Since there transactions of a cooperative game are not done at the individuals level but as a centralized consensus the details of transactions in cooperative games is typically not analyzed.

(ADD MORE DETAIL WHAT THIS IS - and add mathematical examples)

in cooperative games, players communicatewith each other and receive utilities. The concept of cooperative game theory provides answer to the question, “What happens when players communicate with each other and decide to cooperate?”[26].Cooperative game theory consists of two parts: Nash bargaining and coalitional game, Nash bargaininginvolves situations in which a group of players must agree on certain conditions under which they can cooperate. Whereas, the formation of cooperative groups or coalitions are discussed in coalitional game. 
By forming coalitions, players can receive more benefits then they would obtain individually. The players involved in the coalition donot always have the same interest and don’t contribute the same value. The players involved in a coalition expect to receive benefits by forming coalitions, depending on the value they contribute. These players are important for the existence of the coalition and are calledthe coreof the coalition [APPLICATION OF COOPERATIVE GAME THEORYINSMART GRIDSbySpandana Vottem,B.S.A thesis submitted to the Graduate Council ofTexas State University in partial fulfillmentof the requirements for the degree ofMaster of Sciencewith a Major in EngineeringDecember 2019Committee Members:George Koutitas,ChairHarold SternMina Guirguis
]


- The elements of a cooperative game theory are a set of players and a characteristic function

- f the set is formed by all the players of the coalition, it is called agrand coalition. The grand coalition may not always be profitable for all the players,thus it is preferable for some players to form small coalition sets.

-In contrast to grand coalition, empty coalition is a set with no players in it. A proper subsetis a coalition which consists of players less than the total number of players. If the coalition is made from one player, then it is called as  singleton coalition

-Depending on the contribution of the players in the cooperative game, they are divided into three types which are Regular, Dummy and Vetoplayers. Regular players are those who expect payoffs by contributing to the coalition, these players are not important for forming the coalition. Dummy players don’t contribute any value to the coalition but are important to a coalition, due to which theyget some payoff at the end of a game.A player i*is said to be a veto player, if he is involved in all winning coalitions. i*is a veto player if𝑣(𝑁∖𝑖∗)=0[32].

-The characteristic functions of a cooperative game are expected to be super-additive, sub-additive or monotonic. A game is said to be super-additive if the value obtained by the players in coalition is greater than the sum of all values that the players would receive individually. 

-When the worthof a coalition is less than the sum of the worth’sobtained by individual players, the game is said to be sub-additive. 

-Monotonicity means that larger coalitions gain more value, when a coalition Tis greater than coalition S it produces highervalues

-One of the solution typesof cooperative game theory is ‘The Core’. It involvesabout the stability of the coalition instead of fair distribution of payoffs

-Sometimesthe players may forma grand coalition,or some playersmaywish to formsmaller coalitions. As, sometimes players in a smaller coalition gain more profits 

-The sum of payoffs obtained by players in a sub-coalition Sshould be at least equal to the payoff obtained by the players by not forming a coalition. In some games, the core defines the empty set. 

-According to Lloyd Shapley, the benefits are divided among players according to their marginal contributions or the payoff received by each individual player is equivalent tothe valuethey add to the coalition.

-Efficiency:The payoffs should add up to v(N), which means that the surplus of the grand coalition should be allocated among the players.

-Symmetry:If two players iand j contributethe samevalue to every coalition, then iand jare said to be interchangeable w.r.t ‘v’

- Additivity:Thesolution to the sum of two TU (Transfer Utility) games must be the sum of the value obtained by each game

-NullPlayers:A player iis said to be a nullplayer if he doesn’t add any value to the coalition

-he Shapley value is the solution concept of cooperative game theory. In a coalitional game (N,v), the Shapley value divides the total payoff among the players of the game

- he Shapley value describes the marginal contributions
### Non-Cooperative

A sequential game that can be considered is chess. Every step in the game the player needs to understand the possible actions of the other player. Sometimes the best game is when you have all the information available to you to understand the strategy avaialable. Some games do not have all the information available to the player. A game where all the information is avaialable and the players are interchangeable when it comes to rewards then the game is known as a symmetric game. Constant sum games is when all the strategy payoffs can only happen when there is an loss to other players porportionally . A possitive or negative sum game is when all players either benefit or loose given thier available strategies (people working in a company, or competing gangs). In a zero sum game compettition emerges in order to gather the profits at the loss of the other player.

Who wins the game? The idea behind winning a game comes down to identifying the winning strategy and then having the recourses to take actions towards that strategy. In the example provided the question now becomes who will go first player1 or player2 ? If player 1 goes first then player 2 will be forced to take his best course of action and player 1 is assuming this is what player 2 will do because it maximizes its reward. If player 2 goes first the reverse is also true. There are two types of game models Cornout , simultaneous movements between players and Stackelberg is a sequential movement between players. The details of each of these non-cooperative games will be discussed further in subsequent sections.

(Add illustration of 2 games.)
(what a 3 player finite game looks like?)
(ADD MORE DETAIL WHAT THIS IS - and add mathematical examples)


##### Review of Nash Equillibrium

The equilibrium of a non-cooperative game is when either player has no other decisions available that would better thier individual positions. There can be more than one nash equilibrium in a game . An intuitive example is to consider the idea of stop lights in a busy intersection. Both drivers can be considered as players in this game and hte decisions they can take (stop,go) can be expressed in a combinatory manner using the normal-form representation as described before. The rewards for the game can be arbitrarily estimated given the desire of either players. If both players decide to "Go" at the same time then they will end up in a collision. This does not benefit either player so we place the reward for each accordingly (-5,-5). If either of the drivers have to stop to let the other go then the player who is stopped is inconvenience (reward of -1), while the driver who was able to go is now on its way and happy (reward of 1). The final strategy is if both players are stopped and niether move forward wasting time but not in a collision so not as bad but still a loss (reward of -2).

|P1 \ P2|  |     |
|:--:|:---:|:---:|
|   | Go   | Stop   |
| Go | -5,-5 | 1,-1 |
| Stop | -1,1 | -2,-2 |

The possible decisions of the players in the game are mapped out in the game matrix. The strategy for each player can now be assesed. The goal would be to find the best strategies for player 1 and for player 2 respectively. For player 1, the strategy where he is able to go is when player 2 must stop (1,-1). The best strategy for player 2 is the opposite (-1,1). Since there are no better moves for each player to take these are both Nash Equilibriums. The players would decide to move from both of these Nash equilibriums rather than move into any other strategy in the game.

![timeline of GT](./img/3way_intersection.png "Figure 1" =300x)

*Fig. 2. 3-player pay off matrix for 3-way intersection example.*


##### Deeper look at the Stackelberg Model

A Stackelberg Game is a type of noncooperative game that deals with a multi-level decision making process of a number of independent decision makers or players(followers) in response to the decisiont taken by a leading player (the leader) .

- The game has the following components:
  - Followers in the game that respond to a price set by the leader
  - The strategy of each of the followers in terms of satisfying some constraint
  - The utility function of each follower that captures the benefit of consuming the demand
  - The utility function of the leader which captures the total profit
  - The price per unit quantity

The utility function of the follower represents the level of satisfaction of the follower. It is a function of the profit it recieves. The utility function is non-decreasing because each follower is interested in maximizing its profit. The marginal benefit of the follower is also considered a non-increasing function. The marginal benefit gets saturated the closer it gets to the maximum profit. The utility of a follower decreases as the price of a unit or cost of meeting a demand increases .

If the constraint is the same for all players then this gives rise to a noncooperative resource sharing game between the followers. A game like this represents a jointly convex generalized Nash equilibrium problem (GNDP) due to the same shared constraint. In game theory the coupling of the constraints has solution called the Gneralized Nash Equilibirum(GNE).[3]

#### Simulation of Stackleberg Duoply

The stackleberg duoply is a non-cooperative game between two players where one is a leader and the other is a follower. They are the only two players able to supply the needs of the market by creating some quantity of goods. Each player has a utility function that will be satisfied if they can maximize the profit of supply a quantity of goods to the demand curve of the market considering the cost to provide a unit of goods.  [5],[7]

Define a pricing demand as a linear function and call it a "Market Demand Curve"

```
P = a  -  b * Q
```

Where Q is the market quantity demanded and P is the market price in dollars
The firms create the quantity.

The quantity created for the market comes from multiple firms. The firms in a Stackleberg game provide some quantity after the leader firm goes first. The leader firm assumes the moves of the other firms and tries to maximize its profit by incurring the costs to meet the demand that it deems appropriate given its own costs. The demand is met through a total quantity that can be represented by the combination of all of the players quantity. 

```
Q = q1 + q2 + ... qN
```

The cost to meet a single unit of demand per unit qunatity created. This is a pre-defined metric or can be a dynamic value. Knowing the marginal costs is critical to determining the other players moves. The Leader needs to know what it would cost other players to take action.

Begin backward induction to determine what the reaction would be of the other firms. Lets assume two firms A, and B. The procedure to determine the Leaders (firm A) move would be as follows:

1. Calculate Firm B's reaction
2. Calculate Firm A's response to B's reaction
3. Implement Firm A's response
4. Calculate Firm B's response given A's response
5. End Game

$$ N_{firms} = 2$$ (2)
$$ MC_{a} = 10$$ (3)
$$ MC_{b} = 12$$ (4)
$$ P_{T} = -Q_{d}m+b$$ (5)
$$ P_{T} = -Q_{d}*0.5+120$$ (6)

By inspecting the demand curve we can see that all the quantity generated by the payers (x-axis) will result in a total price for all the quantity (y-axis) at different levels of demand met. The pricing demand curve can now be used as a total demand and total quantity output that will be presented to the players. At some break even point the price demand for a unit is no longer advantageous considering the cost to the player to meet that demand.

The break even point would be the profit maximizing point for the player . In the stackleberg game the leader tries to maximize its output by looking at the break even point of the secondary player. If the marginal costs are lower for the follower they can generate more quantity and outsell the leader. This means the leader should make enough to break even and just enough to reduce the gains of the follower.

Again, by only looking at the demand curve the leader can only determine a break even point based on its own cost. As soon as it costs more to meet the demand than the price of the demand then the leader stops and no longer produces. If the demand must be met, then the rest of the demand is left for the second player to take on. If the second player looks at the remaining demand and only supplies what it can break even then both players are left supplying demand with diminishing returns.

To avoid having to supply diminishing returns the leader can take into account the maximizing move for the second player and then include that in determining its stake in the market based on its own costs and break even point.

Total Market Quantity Demand:

$$ Q_{d}= q_{a} + q_{b}$$ (7)

Market Demand Curve:

$$ -0.5*Q_{d} + 120 = -0.5*q_{a} + -0.5*q_{b} + 120$$ (8)

$$ TR_{b} = -0.5*q_{a}*q_{b} - 0.5*q_{b}^2 + 120*q_{b}$$ (9)

Marginal revenue can be derived from the derivative of the total revenue equation (9), with respect to the firm.

$$ MR_{b} = \frac{\partial d}{\partial q_{b}}(-0.5*q_{a}*q_{b} - 0.5*q_{b}^2 + 120*q_{b})$$ (10)
$$ MR_{b} = -0.5*q_{a} - q_{b} + 120$$ (11)

The reaction of the follower can be estimated by the leader by solving when the marginal cost of the follower will equal the marginal revenue of the follower. Setting them equal and solving for the quantity in terms of the quantity provided by the leader firm A we get the following reactionary quantity for firm B.

$$ q_{b}^* = -0.5*q_{a} + 108$$ (12)

The leader takes into account all the reactions and creates a leader response to the reactions. The approach is to use back induction to take the forecasted reaction of the follower when the marginal cost is equal to the marginal revenue (profit maximizing). That means that the follower will stop at some break even point that maximizes its profits. Given that information the leader can take that reaction and assume it is what the follower will do. The assumption is used in the price demand formula. By substituting equation (12) into equation (8) the demand for the leader is now shown below in (13). Knowing the demand the total revenue and marginal revenue can also be inferred.

$$ P_{leader} = -0.25*q_{a} + 66$$ (13)
$$ TR_{a} = -0.25*q_{a}^2 + 66*q_{a}$$ (14)
$$ MR_{a} = \frac{\partial d}{\partial q_{a}}(-0.25*q_{a}^2 + 66*q_{a})$$ (15)
$$ MR_{a} = -0.5*q_{a} + 66$$ (16)

The last step in the backwards induction for the leader is to try to maximize his profit by only providing a quantity where the followers quantity has been considered in the game. The final quantity to be implemented by the leader is done just as before by setting marginal revenue equal to marginal cost and finding quantity.

$$ q_{a}^Final = 112$$ (17)

If we implement the leaders quantity output and then recalculate the resulting quantity for the follower, the follower will have a different output than what was orginally measured by the leader since the leader has now taken its maximum demand.

$$ q_{b}^Final = 52$$ (18)


#### Evolutionary

The Crafoord Prize in 1999 (which is the highest prize in Biological Sciences), went  to  John  Maynard  Smith  (along  with  Ernst  Mayr  and  G.  Williams)  “for developing  the  concept  of  evolutionary  biology,”  where  Smith’s  recognized  contributions  had  astrong  game-theoretic  underpinning,  through  his  work  on  evolutionary  games  and  evolutionary stable equilibrium.[5]

Compared with classic game theory, the Evolutionary Game Theory (EGT) takes the population as the research object, and believes that the game individual is bounded rational, and the strategy of the individual game may change due to the variation. Thus, EGT is more inline with the realistic game situation because it adopts the mechanism of natural selection and does not require strict rational assumptions. [5]. The problem with EGT is choosing the selection and mutation mechanisms and making them represent actual issues is very challenging. [9]

A fundamental goal of evolutionary game theory is to understand how the individual organisms in biological system or social system interact with each other, and evolve over time with the environment determine the spatial distribution of populations and the structure of communities. It considers a population of players interacting in a game with fixed strategies and payoff of each individual is interpreted as fitness, and success in the game is translated into reproductive success.[15]


#### Different Game Models

The different types of models as defined in [4] consists of the following:

1) Ordinary non-cooperative game: The establishment of ordinary non-cooperative game model is no longer a difficult thing.  The  basic  idea  is  to  analyze  the  problem,  abstract  the  three  elements  of  modeling,  establish  model,  analyze  the  properties of equilibrium solution and solve the problem.

2) Generalized  Nash  equilibrium  game:  Each  player’s  decision affects not only other players’ payoffs, but also their feasible strategies set.

3) Cournot   game:   It   is   the   earliest   version   of   the   application  of  Nash  equilibrium  and  a  classic  case  in  game  theory,   which   is   also   well-known   as   a   special   case   of   prisoner’s dilemma model.

4) Stackelberg  game:  It  is  the  simplest  model  of  a  leader-follower  game,  in  which  the  follower  can  know  well  about  the  leader’s  behavior  and  previous  game  information  and the leader can predict the follower’s action before making a decision.

5) Bounded  rationality  game:  While  game  theory  has  acquired  great  success,  some  people  have  questioned  the  assumption that the players are completely rational. Bounded rational game is much closer to reality because it is based on the assumption that each player desires the best result but can only get limited payoffs.

6) Repeated game: Made up of a few repeated basic games, each stage of a repeated game is a complete game. Although repeated game is just a repetition of basic games in the form, but the result could be quite different.




### Repettetive Game Play

A computer simulation playing itterative games of the prisoners dillema in Robert Axelrods book "Evolution of Cooperation" was shown to play a game called Tit-for-Tat that would outperform any other game strategy[2]. In this strategy the simulation would mimic human like behaviour that would act in synchronicity to how anohter player acts towards it i.e. positive reaction would result in a positive reaction and vice-versa, but when a negative reaction occured it would be best to return a negative reaction and then go back to a positive reaction. This strategy would be effective as long as the players did not repeat negative actions towards each other , otherwise it would spiral into repeated negative actions until both are destroyed.

## Appendix

### Python Stakelberg Duopoly Simulation
```python 
from sympy import * 
init_printing(use_latex='mathjax')
from IPython.display import display
import string
alpha = list(map(chr, range(97, 123)))

firms = 2

N = symbols('N_{Firms}')
display(Eq(N,firms))

# Marginal Cost
MC = [symbols('MC_%s'% i) for i in alpha]
for i in range(firms):
    cost = 10 + i*2
    display(Eq(MC[i],cost))
    MC[i]=cost

# General Market Demand Curve
b,m = symbols('b,m')
P_d = symbols('P_{T}')
Q_d = symbols('Q_{D}')
display(Eq(P_d,b-m*Q_d))
b = 120
m = 0.5
display(Eq(P_d,b-m*Q_d))
P_d=b-m*Q_d

# Total Market Quantity Demand
q = [symbols('q_%s'% i) for i in alpha]
Q = sum(q[i] for i in range(firms))
display(Eq(Q_d,Q))

# Market Demand Curve
P = b - m * Q
display(Eq(P_d,P))

# Total Revenue
TR = [symbols('TR_%s'% i) for i in alpha]
for i in range(firms-1):
    display(Eq(TR[i+1],expand(P * q[i+1])))
    TR[i+1]= expand(P * q[i+1])

# Marginal Revenue
MR = [symbols('MR_%s'% i) for i in alpha]
for i in range(firms-1):
    display(Eq(MR[i+1],Derivative(TR[i+1],q[i+1])))
    display(Eq(MR[i+1],Derivative(TR[i+1],q[i+1]).doit()))
    MR[i+1]= Derivative(TR[i+1],q[i+1]).doit()

# Reaction Functions :
qq = [symbols('q^{*}_%s'% i) for i in alpha]
for i in range(firms-1):
    display(Eq(qq[i+1],solve(MR[i+1] - MC[i+1],q[i+1])[0]))
    qq[i+1]=solve(MR[i+1] - MC[i+1],q[i+1])[0]

# Leaders market demand in terms of leader quantity
P_0 = P 
P_a = symbols('P_Leader')
for i in range(firms - 1) :
    P_0 = P_0.subs(q[i+1],qq[i+1])

display(Eq(P_d,P))

display(Eq(P_a,P_0))

TR_0 = expand(P_0 * q[0])
TR_a = symbols('TR_a')
display(Eq(TR_a,TR_0))

MR_0 = Derivative(TR_0,q[0]).doit()
MR_a = symbols('MR_a')
display(Eq(MR_a,Derivative(TR_0,q[0])))
display(Eq(MR_a,MR_0))

# Most profit maximizing quantity for leader is q_0
q_0 = solve(MR_0-MC[0],q[0])[0]
q_a = symbols('q^Final_a')
display(Eq(q_a,q_0))

# Reactions Taken :
qqq = [symbols('q_%s__Final'% i) for i in alpha]
for i in range(firms-1):
    display(Eq(qqq[i+1],qq[i+1].subs(q[0],q_0)))
    qqq[i]=qq[i+1].subs(q[0],q_0)
P_d=b-m*Q_d
display(Eq(Q_d,Q))
q[0] = q_0
for i in range(firms-1):
    q[i+1] = qqq[i]
```




---

[figure1]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"
[figure2]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"
