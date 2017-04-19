#!/usr/bin/env python
import sys

fav_trips = {}
for line in sys.stdin:
    line = line.strip()
    if "\t" not in line:
        continue
    key,area_info = line.split("\t")
    data = key.split(",")
    areas = area_info.split(",")
    if len(data)<18 or data[0]=="vendor_id" or data[0]=="VendorID":
        continue
    if areas[1]=="NA" or areas[3]=="NA":
        continue
    if fav_trips.get(areas[1]+","+areas[3]):
        fav_trips[areas[1]+","+areas[3]]+=1
    else:
        fav_trips[areas[1]+","+areas[3]]=1
for key in fav_trips.keys():
    print str(key)+"\t"+str(fav_trips[key])
