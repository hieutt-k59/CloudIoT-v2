from pymongo import MongoClient
from datetime import datetime
client = MongoClient()

db = client.IoTDb
a = []
data = db.devices.find({'device':'sensor_1'})
for document in data:
    t = datetime.strptime(document['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
    a.append(int(t.year))
print (a)
