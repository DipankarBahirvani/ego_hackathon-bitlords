
# coding: utf-8

# In[ ]:


from confluent_kafka import Consumer, KafkaError
from influxdb import InfluxDBClient
import time 
import json
import datetime
import random


c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})
user = 'root'
password = 'root'
dbname = 'vehicle'
json_body=[]
data={}
data["measurement"] = "vehicle_signals"
tag={}
tag["vachicle_id"]= "ec0e7d95-562e-4de3-b3f6-8f2cd6113d22"
tag["location"]="Aachen"
data["tags"]=tag
client = InfluxDBClient('localhost', 8086, user, password, dbname)

c.subscribe(['vehicle_signals'])

while True:
    try:
        msg = c.poll(1.0)

    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break

    if msg is None:
        continue

    if msg.error():
        print("AvroConsumer error: {}".format(msg.error()))
        continue

    print(msg.value().decode('utf-8'))
    json_body=[]
    data["time"]= datetime.datetime.utcnow()
    data["fields"]= json.loads(msg.value().decode('utf-8'))
    json_body.append(data)
    print(json_body)
    try :
        client.write_points(json_body)
    except :
        print("Error")
     

c.close()

