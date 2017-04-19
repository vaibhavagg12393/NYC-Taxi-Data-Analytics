#!/usr/bin/env python
import sys
previous_key = None
num_trips = 0
tot_fare = 0
tot_seconds = 0
for line in sys.stdin:
    key, value = line.split("\t")
    values = value.split(",")
    if not previous_key or previous_key == key:
        num_trips += 1
        tot_fare += float(values[0])
        tot_seconds += float(values[1])
    else:
        if num_trips!=0:
            avg_fare = float(tot_fare)/num_trips
            avg_seconds = float(tot_seconds)/num_trips
            print previous_key+"\t"+str(avg_fare)+","+str(avg_seconds)
        tot_fare = float(values[0])
        tot_seconds = float(values[1])
        num_trips = 1
    previous_key = key
if num_trips!=0:
    avg_fare = float(tot_fare)/num_trips
    avg_seconds = float(tot_seconds)/num_trips
    print previous_key+"\t"+str(avg_fare)+","+str(avg_seconds)
