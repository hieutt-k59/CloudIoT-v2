import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'RbiCloud.settings'
application = get_wsgi_application()

from cloud import models
import paho.mqtt.client as mqtt
import json
from datetime import datetime
# from cloud.process.RBI import fastCalulate as ReCalculate
from pymongo import MongoClient
#Connect to MongoDB
dbClient = MongoClient("localhost", 27017)
# db_name = "IoTDb"
# collection_name = "devices"
db = dbClient.IoTDb
collection = db.devices
# This is the Subscriber
TOPIC = "+/+"
def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC, 0)
    print("Connected MosquittoMQTT with result code: " + str(rc))
# def on_subcribe(client, obj, mid, granted_qos):
#     print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_log(client, obj, level, string):
    print(string)
def on_message(client, userdata, msg):
    split_arr = (str(msg.topic)).split('/')
    payload = msg.payload.decode()
    data = json.loads(payload)
    str_type = split_arr[0]
    print("Type message: " + str_type)
    print(data)
    devices_collection = db.devices
    devices_collection.insert_one(data)

    print("Finished!")
    
    # client.disconnect()

CLOUD_URL = 'localhost'

PORT = 1883
client = mqtt.Client()
client.connect(CLOUD_URL,PORT)

client.on_connect = on_connect
client.on_message = on_message