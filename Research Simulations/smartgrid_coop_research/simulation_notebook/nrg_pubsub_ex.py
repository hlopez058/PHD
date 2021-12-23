import threading
import paho.mqtt.client as mqtt
import json
import pandas as pd
import time
mqttBroker = "localhost"
mqttPort = 1883  # port for mosquitto broker
client = mqtt.Client("client1")  # create new instance
msg_dict = []  # create a list to store the messages


def main():
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_message = on_message  # Define callback function for receipt of a message
    client.connect(mqttBroker, mqttPort, 60)  # Connect to the broker
    client.loop_forever()  # Start networking daemon


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe("INFO")


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
            tp = df[df['kW'] > 0].groupby(['time']).sum()
            tc = df[df['kW'] < 0].groupby(['time']).sum()
            # itterate through values of tp
            for index, row in tp.iterrows():
                # update df with tp at time index
                df.loc[df['time'] == index, 'tp'] = row['kW']
            for index, row in tc.iterrows():
                # update df with tc at time index
                df.loc[df['time'] == index, 'tc'] = row['kW']
            time.sleep(2)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    threading.Thread(target=thread_process_msgs, args=(1,)).start()
    main()
    p2p_meter_msg = {
        'time': 1637984408,
        'qos': 0,
        'id': 1,
        'kW': 0.12,
    }
