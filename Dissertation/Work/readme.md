







Use of MQTT Broker
- A Publish/Subscribe protocol for IoT 
- Used to replicate an exchange market
- Used to handle multiple topics so that "bots" could interact

Topics:
- HourlyMarketState:
    - What Publishing cycle we are on?
        - Gate Closure for that publshing cycle , for a given bidding period
    - Whate energy exchange cylce are we on?
        - when does this energy echange time end?
    - What hour is currently settling?
        - when was the bill date for this?
        - what exchange hour is settling
        - what bids for this settlement?

- Orders:
    - can be placed cancelled and modified by peers only before the gate closure
    - orders are tied to a bidding period (when submitted)

- ItemList : 
    - offers of available generation with "start" duration, and amount from sellers
    - typically surplus energy over half an hour for sale


The generation and consumption of the bots should be dependent on a global trend and then updated as needed for each bots particular consumption or generation limitations.

- SolarOutput : 
    - provides changes of irridiance for bots 
    - also provides forecast for future changes?

- TypicalConsumptionCurve:
    - a topic with base consumption curve for every hour

Model of the Supplier
- Generation source (PV)
    - would need some kind of trend of what is generated
    - requires a connection to an atomic clock counter
    - could also reference a topic for irridiance


bots.. can be crreated on seperate threads
elecbay needs to process orders that it recieves.
return the order post with "accepted/rejected"

bots can now order from elecbay

elecbay needs to have a sequence that changes
between states?

also the bots need to be synchronized with the elecbay

can i build a topic that has a timer?
should elecbay just coordinate? with its own internal timer?

build a publish topic so buyers can browse available items to purchase?
