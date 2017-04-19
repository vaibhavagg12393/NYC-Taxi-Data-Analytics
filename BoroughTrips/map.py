#!/usr/bin/env python
import sys

boroughs = {}
for line in sys.stdin:
    line = line.strip()
    if "\t" not in line:
        continue
    key,area_info = line.split("\t")
    data = key.split(",")
    areas = area_info.split(",")
    if len(data)<18 or data[0]=="vendor_id" or data[0]=="VendorID":
        continue
    if areas[0]=="NA":
        continue
    if boroughs.get(areas[0]):
        boroughs[areas[0]]+=1
    else:
        boroughs[areas[0]]=1
for key in boroughs.keys():
    print str(key)+"\t"+str(boroughs[key])
