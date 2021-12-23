#!/usr/bin/bash
for i in `seq 100`
do
sudo python3 LoadBalancer_method2.py
sudo python3 measure_evaluation_InsertDB.py
sleep 20
done
