#!/usr/bin/env python
import sys
import datetime

def convert_str_to_date(date_str):
    date_obj = None
    try:
        date_obj = datetime.datetime.strptime(date_str,'%Y-%m-%d %H:%M:%S')
    except Exception:
        pass
    return date_obj

days = {}
for line in sys.stdin:
    line = line.strip()
    data = line.split(",")
    if len(data)<18 or data[0]=="vendor_id" or data[0]=="VendorID":
        continue
    date_obj = convert_str_to_date(data[1])
    if days.get(date_obj.date().__str__()):
        days[date_obj.date().__str__()]+=1
    else:
        days[date_obj.date().__str__()]=1
for key in days.keys():
    print str(key)+"\t"+str(days[key])
