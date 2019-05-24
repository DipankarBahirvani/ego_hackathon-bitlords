#  HACKATHON 

###  Setup of technlogies 

* python 3.6 
* Grafana  (https://grafana.com/docs/installation/)
* InfluxDB (https://docs.influxdata.com/influxdb/v1.7/introduction/installation/)
* Nifi  (https://nifi.apache.org/docs/nifi-docs/html/getting-started.html)
* Kafka (https://kafka.apache.org/)
* RStudio
 

### Start  the services 
* `sudo service grafana-service start`
* `sudo service influxdb start`
* `./confluent start`
*` /opt/nifi-1.9.0/bin and run ` and type `./nifi status` 



## URL for grafana and nifi
* http://localhost:3000
* http://localhost:8080/nifi


## Install python modules 
* pip install requirements.txt
* python hackathon/code_base/python_scripts/get_signals.py &
* python hackathon/code_base/python_scripts/kafka_producer.py &
* python hackathon/code_base/python_scripts/InfluxWriterKafka.py.py &

