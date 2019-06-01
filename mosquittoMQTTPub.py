import paho.mqtt.client as mqtt
import json
import argparse
from datetime import datetime
import random
import time
# from cloud.process.RBI import DM_CAL

# This is the Publisher
# d = DM_CAL.DM_CAL(HighlyEffectDeadleg=True, ContainsDeadlegs=False, OnlineMonitoring="Sulfuric acid (H2S/H2) corrosion high velocity - Key process parameters")
# print(d.DF_THIN(5.08))
init_tem = 33.33

def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_ip', default='localhost', help='Server IP address')
    parser.add_argument('--port', default=1883, help='Port listen')
    # parser.add_argument('--u', defaul='$ACCESS_TOKEN', help="User access token")
    return parser.parse_args()
def publish_data(val, type_data):
    args = parse_command_line_args()
    CLOUD_URL = args.server_ip
    PORT = int(args.port)
    client = mqtt.Client()
    client.connect (CLOUD_URL, PORT, 60)
    data = {'device':'sensor_1', 'value': val, 'type':type_data, 'timestamp':str(datetime.now())}
    print(data['device'])
    send_data = json.dumps(data)
    client.publish("data/adfadfadfasf", send_data)
    client.disconnect()
def main():
    args = parse_command_line_args()
    tem = 33.33
    type_data = 'tem'
    for i in range(23):
        publish_data(tem, type_data)
        print(str(i+1) + ". Data was sent at " + str(datetime.now()))
        time.sleep(2)
        tem = tem + random.random()

if __name__ == "__main__":
    main()


