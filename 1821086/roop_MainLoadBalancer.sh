#!/usr/bin/bash
for i in `seq 100000`
do
sudo python MainLoadBalancer.py
sudo python measure_evaluation_InsertDB.py
sleep 30
done
