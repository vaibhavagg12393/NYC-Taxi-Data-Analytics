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

def is_weekend(date_obj):
    return date_obj.weekday==5 or date_obj.weekday==6

for line in sys.stdin:
	data = line.strip().split(",")

	if len(data)<18 or data[0] == "vendor_id" or data[0]== "VendorID" :
		continue

	rate_code = data[7]
	dropoff_date_time = data[2]
	date_obj = convert_str_to_date(dropoff_date_time)
	month1 = date_obj.month

	print str(month1) + "\t" + str(rate_code)
