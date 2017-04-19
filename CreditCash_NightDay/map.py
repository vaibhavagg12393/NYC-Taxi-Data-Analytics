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


def get_time_range(date_obj):
    if date_obj.hour>=5 and date_obj.hour<=21:
        return "day"
    else:
        return "night"

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) < 18 or data[0] == "vendor_id" or data[0]=="VendorID":
       continue
    payment_type = data[11]
    pickup_datetime = data[1]

    date_obj = convert_str_to_date(pickup_datetime)
    time_range = get_time_range(date_obj)
    print str(time_range) + "\t" + payment_type
