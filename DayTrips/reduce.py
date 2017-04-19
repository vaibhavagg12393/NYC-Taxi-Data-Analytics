#!/usr/bin/env python
import sys
import operator
previous_key = None
total = 0
top_days = {}
for line in sys.stdin:
    key, value = line.split("\t")
    if not previous_key or previous_key == key:
        total += int(value)
    else:
        top_days[previous_key]=total
        total = int(value)
    previous_key = key
if previous_key:
    top_days[previous_key]=total
sorted_top_days = sorted(top_days.items(), key=operator.itemgetter(1), reverse=True)
for key,value in sorted_top_days:
    print str(key)+"\t"+str(value)
