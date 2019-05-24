
# coding: utf-8

# In[ ]:


import requests
import json
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import csv
import time
import random






header = {
    
    'X-API-KEY': 'ec0e7d95-562e-4de3-b3f6-8f2cd6113d22',
    "Accept": "application/json",
    "Content-Type": "application/json"
    
}

def get_payload() : 
    payload = {}
    payload["battery_charging"] = random.choice(["yes","no"])
    payload["battery_health"] = random.randrange(0,101,1)
    payload["mileage"] = random.randrange(0,10000,1)
    payload["speed"] = random.randrange(0,180,1)
    payload["central_locking_system"] = random.choice(["closed","open"])
    payload["rain_sensor"] = random.choice(["rain","no_rain"])
    payload["distance_to_object_back"] = random.uniform(0,20)
    payload["distance_to_object_front"] = random.uniform(0,20)
    payload["distance_to_object_bottom"] = random.uniform(0,20)
    payload["distance_to_object_left"] = random.uniform(0,20)
    payload["distance_to_object_right"] = random.uniform(0,20)
    payload["temperature_inside"] = random.randrange(-100,100,1)
    payload["temperature_outside"] = random.randrange(-100,100,1)
    payload["person_count"] = 3 
    return payload









url = "https://ego-vehicle-api.azurewebsites.net/api/v1/vehicle/signals"


# In[ ]:


while True:
    time.sleep(2)
    r = requests.patch(url, json=get_payload() , headers=header)
    print(r)
    

