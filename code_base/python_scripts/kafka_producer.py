
# coding: utf-8

# In[12]:


from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import csv
import time

from datetime import datetime
import requests



def get_producer():
    #value_schema = avro.load("factory_floor1_machine_1_parameters.avsc")

    #avroProducer = AvroProducer({
       # 'bootstrap.servers': '0.0.0.0:9092',
    #'schema.registry.url': 'http://localhost:8081'
    #    },  default_value_schema=value_schema)
   # return avroProducer
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    return producer











# In[13]:


MQTT_TOPIC="vehicle/signals"
KAFKA_TOPIC=MQTT_TOPIC.replace("/","_")




headers = {
    
    'X-API-KEY': 'ec0e7d95-562e-4de3-b3f6-8f2cd6113d22',
    
}

avroProducer=get_producer()
KAFKA_TOPIC = MQTT_TOPIC.replace("/","_")

while True :
    time.sleep(2)
    message = requests.get('https://ego-vehicle-api.azurewebsites.net/api/v1/vehicle/signals?cache=0', headers=headers)
    try :
        message= (json.loads(message.content.decode("utf-8")))
    except :
        print("Message cannot be parsed")
        
    print(message)
    try :
        avroProducer.send(topic=KAFKA_TOPIC, value=message)
        avroProducer.flush()
    except :
        print("Avro failure Kafka")
        

   
    




