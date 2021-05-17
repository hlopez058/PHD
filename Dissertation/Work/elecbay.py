import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import json
client = mqtt.Client("elecbay_market")
mqttBroker = "127.0.0.1" #"iot.eclipse.org" #"iot.eclipse.org" #"test.mosquitto.org"

def main():
    client.on_message=on_message
    client.connect(mqttBroker)
    client.subscribe([('market/order',0),('market/offer',0)])
    client.loop_start() # seperate thread for listening
    start_bidding()
    time.sleep(30)
    stop_bidding()
    client.loop_stop()
    client.unsubscribe('market/order')
    print("elecbay-shutdown")


def start_bidding():
    msg = {
            "uid" : 9999,
            "requester" : "elecbay", 
            "type" : "bidding",
            "state" : "none",
            "value" : "open",
            "duration" : 30
        }
    client.publish('elecbay/bidding',json.dumps(msg))

def stop_bidding():
    msg = {
            "uid" : 9999,
            "requester" : "elecbay", 
            "type" : "bidding",
            "state" : "none",
            "value" : "closed"
        }
    client.publish('elecbay/bidding',json.dumps(msg))


def on_message(_client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    msg = json.loads(str(message.payload.decode("utf-8")))
    if msg['type'] == 'order' :
        process_order(msg)
    if msg['type'] == 'item' :
        process_item(msg)

def process_item(msg):
    if msg['state'] == 'pending':
        msg['state'] = 'accepted'
        item = json.dumps(msg)
        client.publish('elecbay/item',item)
        print(f'published : {item}')

def process_order(msg):
    if msg['state'] == 'pending':
        msg['state'] = 'accepted'
        order = json.dumps(msg)
        client.publish('elecbay/order',order)
        print(f'published : {order}')

if __name__ == "__main__":
    main()