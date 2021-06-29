import random
import math
import enum

from sklearn.linear_model import LinearRegression

class Buyer:
    def __init__(self):
        self.meter_reads = []
        self.order = {}
    def prepayment():
        return  5
    def browse(self, items):
        # look at all items
        # find one that works 
        # offer a bid for the item
        # store as an order request
        return  0
    def bid(self):
        # update order with bid
        return self.order

    def accept_order_n_deliver():
        return  5
    def get_required_energy():
        return 30

class Seller:
    def __init__(self):
        self.meter_reads = []
    def prepayment():
        return  5
    def listing_items():
        return  5
    def accept_order_n_deliver():
        return  5
    def get_meter_read(self,t):
        trend = math.sin(t)    
        self.meter_reads.append(trend * random.randrange(0,10))
        return 
    def get_forecasted(self,dt):
        X = list(range(1,len(self.meter_reads))) # put your dates in here
        y = self.meter_reads   # put your kwh in here
        model = LinearRegression()
        model.fit(X, y)
        X_predict = [len(X)+dt]  # put the dates of which you want to predict kwh here
        y_predict = model.predict(X_predict)
        return y_predict

def main():
    N=3
    simulation_hours = list(range(1,5280))
    buyers = [ Buyer() for buyer in N ]
    sellers = [ Seller() for seller in N ]
    elecbay = ElecBay()

    # t is 0.5 hourly intervals
    for t in simulation_hours:
        # Publishing and Bidding 
        if elecbay.state == ElecbayProcessing.Publishing_and_Bidding:
            # This period can start several days,weeks,months 
            # ends before the half-hourly energy exchange time period
            # the ending is called the gate closure

            # Sellers post what they are willing to offer as items
            [ elecbay.publish(seller.items) for seller in sellers]
            # Buyers can browse the offereed items 
            [ buyer.browse(elecbay.item_queue) for buyer in buyers]
            # Buyers can then order the items from elecbay as bids
            [ elecbay.bidding(buyer.order) for buyer in buyers]

        # Orders can be placed, canceled or modified by peers only before the 
        # gate closure


        #Gate closure
        #Energy Exchange
        #Bill Date
        #Settlement

class ElecBay:
    def __init__(self):
        self.order_queue = []
        self.item_queue = []
        self.state = 0

    def place_order(self):
        status= 'accepted'
        if self.get_network_constraint() != 'none':
            status= 'rejected'
        return status
    def provide_energy_balancing_service():
        pass
    def get_network_constraint(self):
        constraints = {"none","voltage cexcursion","thermal overloading"}
        return random.choice(list(constraints.values())) 
    
    def bidding(self,order):
        # receive orders and put them in a queue
        self.order_queue.append(order)

    def publish(self,item):
        # receive item and put them in a queue
        self.item_queue.append(item)

class Item:
    amount_of_energy = 10
    duration_of_energy = 30 

class Order :
    time_period_hour_starting = 1
    time_period_hour_ending = 2
    amount_of_energy = 1
    price_of_energy = 1
    buyer_id = 1
    seller_id = 1

class PowerImbalanceService:
    x=5

# Using enum class create enumerations
class ElecbayProcessing(enum.Enum):
   Publishing_and_Bidding = 1
   Gate_Closure = 2
   Energy_Exchange = 3
   Bill_Date = 4
   Settlement = 5


