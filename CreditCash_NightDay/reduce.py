#!/usr/bin/env python
import sys
previous_key = None
payment_type = {}
for line in sys.stdin:
    key, value = line.strip().split("\t")

    if not previous_key or previous_key == key:
        if value == "":
            continue
        value = value.lower()
        if payment_type.get(value):
            payment_type[value] +=1
        else:
            payment_type[value] = 1
    else:
        total = 0.0
        for i in payment_type.keys():
            total+=payment_type[i]
        print (previous_key+"\t"),
        for i in sorted(payment_type.keys()):
            print (str(i)+":"+str((payment_type[i]/total)*100) +","),
        print ""
        value = value.lower()
        payment_type = {}
        payment_type[value] = 1
    previous_key = key
if previous_key:
    total = 0.0
    for i in payment_type.keys():
        total+=payment_type[i]
    print (previous_key+"\t"),
    for i in sorted(payment_type.keys()):
        print (str(i)+":"+str((payment_type[i]/total)*100) +","),
    print ""
