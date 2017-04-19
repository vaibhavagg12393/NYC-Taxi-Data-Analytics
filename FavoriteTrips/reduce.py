#!/usr/bin/env python
import sys
import operator
fav_trips = {}
for line in sys.stdin:
    key, value = line.split("\t")
    if fav_trips.get(key):
        fav_trips[key]+=int(value)
    else:
        fav_trips[key]=int(value)
sorted_fav_trips = sorted(fav_trips.items(), key=operator.itemgetter(1),reverse=True)
for i in range(min(10,len(sorted_fav_trips))):
    print sorted_fav_trips[i][0]+"\t"+str(sorted_fav_trips[i][1])
