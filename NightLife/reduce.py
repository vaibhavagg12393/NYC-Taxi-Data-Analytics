#!/usr/bin/env python
import sys
import operator
month_dict = {}
for line in sys.stdin:
    key,value = line.strip().split("\t")
    values = key.split(",")
    d = month_dict.get(int(values[0]))
    if d:
        if d.get(values[1]+","+values[2]):
            d[values[1]+","+values[2]]+=int(value)
        else:
            d[values[1]+","+values[2]]=int(value)
    else:
        d = {}
        d[values[1]+","+values[2]]=int(value)
        month_dict[int(values[0])] = d
for key in sorted(month_dict.keys()):
    sorted_d = sorted(month_dict[key].items(), key=operator.itemgetter(1), reverse=True)
    for i in range(min(10,len(sorted_d))):
        print str(key)+","+str(sorted_d[i][0])+"\t"+str(sorted_d[i][1])
