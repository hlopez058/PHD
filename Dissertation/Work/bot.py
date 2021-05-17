from collections import OrderedDict
from elecbay import stop_bidding
import paho.mqtt.client as mqtt
import time
import json
from random import randrange, uniform
from threading import Thread
import logging
from datetime import datetime,timedelta

class BuyerBot:
    def __init__(self,id):
        self.id =id
        self.client = mqtt.Client("elecbay_market_buyer" + str(self.id))
        self.mqttBroker = "127.0.0.1" #"iot.eclipse.org" #"iot.eclipse.org" #"test.mosquitto.org"
        self.can_bid = False
        self.approved_orders = []
        self.rejected_orders = []
        self.offered_items = []

    def on(self):
        logging.info("Thread buyer-bot-%s: starting", self.id)
        self.client.on_message=self.on_message
        self.client.connect(self.mqttBroker) 
        self.client.subscribe([('elecbay/item',0),('elecbay/order',0),('elecbay/bidding',0)])
        self.client.loop_start() # seperate thread for listening    
        time.sleep(3)
        while self.can_bid:
            items = self.browse()
            self.bid(items)    
        self.clear_bidding_process()
        #self.consume_energy()

    def consume_energy(self):
        # search a topic for energy provided
        # detect if its available
        logging.info(f"buyer-bot-{self.id} : has consumed energy")

    def on_message(self,_client, userdata, message):
        #print("received message: " ,str(message.payload.decode("utf-8")))
        msg = json.loads(str(message.payload.decode("utf-8")))
        if str(msg['uid']) == str(self.id) and msg['type'] == 'order' :
             self.process_order(msg)
        if msg['type'] == 'bidding' :
            if msg['value'] == 'open':
                self.can_bid = True
            else:
                self.can_bid = False
        if msg['type'] == 'item' :
             self.process_item(msg)
        
    def clear_bidding_process(self):
        self.approved_orders = []
        self.rejected_orders = []
        self.offered_items = []

    def bid(self,items):
        for item in items :
            msg = {
                        "uid" : self.id,
                        "requester" : "buyer-bot-" + str(self.id), 
                        "type" : "order",
                        "state" : "pending",
                        "value" : uniform(0.0, 10.0),
                        "duration" : 1 ,
                        "source" : item
                    }        
            order = json.dumps(msg)
            self.client.publish('market/order',order)
            logging.info(f"buyer-bot-{self.id} : has placed a bid on offering from {item['requestor']}")


    def browse(self):
        items = []
        minimum_energy_required = 1.5
        for item in self.offered_items:
            if item['value'] > minimum_energy_required:
                start_time = datetime.strptime(item['start_time'],'%H:%M:%S')
                crit_time = (datetime.now() + timedelta(seconds=5))
                if  start_time < crit_time:
                    items.append(item)
                    logging.info(f"buyer-bot-{self.id} : has found an offer from {item['requestor']} for energy at {item['start_time']}.")
        return items

    def process_item(self,msg):
        #look for offerings that fit critieria
        if msg['state'] == 'accepted' :
                self.offered_items.append(msg)

    def process_order(self,msg):
        if msg['state'] == 'rejected' :
            self.rejected_orders.append(msg)
            #print('bot[',self.id,']: ',"order was rejected, going to process")       
        if msg['state'] == 'accepted' :
            self.approved_orders.append(msg)
            logging.info(f"buyer-bot-{self.id} : bid order has been accepted ; expecting energy exchange from {msg['source']['requestor']} for {msg['source']['value']} at time {msg['source']['start_time']}")



class SellerBot:
    def __init__(self,id):
        self.id =id
        self.client = mqtt.Client("elecbay_market_seller" + str(self.id))
        self.mqttBroker = "127.0.0.1" 
        self.can_offer = False
        self.approved_items = []
        self.rejected_items = []
    
    def on(self):
        logging.info("Thread seller-bot-%s: starting", self.id)
        self.client.on_message=self.on_message
        self.client.connect(self.mqttBroker) 
        self.client.subscribe([('elecbay/item',0),('elecbay/bidding',0)])
        self.client.loop_start() # seperate thread for listening    
        time.sleep(5)
        while self.can_offer  :
            self.offer()
            time.sleep(5)
        self.clear_bidding_process()
        self.client.loop_stop()
        
    def clear_bidding_process(self):
        self.approved_items = []
        self.rejected_items = []
          
    def on_message(self,_client, userdata, message):
        msg = json.loads(str(message.payload.decode("utf-8")))
        #print("seller received message: " ,msg)
        if str(msg['uid']) == str(self.id) and msg['type'] == 'item' :
             self.process_item(msg)
        if msg['type'] == 'bidding' :
            if msg['value'] == 'open':
                self.can_offer = True
            else:
                self.can_offer = False

    def offer(self):
        msg = {
                    "uid" : self.id,
                    "requestor" : "seller-bot-" + str(self.id), 
                    "type" : "item",
                    "state" : "pending",
                    "value" : uniform(0.0, 10.0),
                    "duration" : 1, 
                    "start_time" : (datetime.now() +  timedelta(seconds=10)).strftime('%H:%M:%S'),
                    "end_time": (datetime.now()  + timedelta(seconds=11)).strftime('%H:%M:%S')
                }        
        item = json.dumps(msg)
        self.client.publish('market/offer',item)
        logging.info(f"seller-bot-{self.id} : has published offering")

    def process_item(self,msg):
        if msg['state'] == 'rejected' :
            self.rejected_items.append(msg)
        if msg['state'] == 'accepted' :
            self.approved_items.append(msg)
    

def launchBuyerBot(id):
    buyer = BuyerBot(id)
    buyer.on()
def launchSellerBot(id):
    seller = SellerBot(id)
    seller.on()

def main():        
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

    threads = list()
    for index in range(1):
        logging.info("Main    : create and start thread %d.", index)
        x = Thread(target=launchBuyerBot, args=(index,))
        y= Thread(target=launchSellerBot, args=(index + 100,))
        x.setDaemon(True)
        threads.append(x)
        y.setDaemon(True)
        threads.append(y)
        x.start()
        y.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

if __name__ == "__main__":
    main()