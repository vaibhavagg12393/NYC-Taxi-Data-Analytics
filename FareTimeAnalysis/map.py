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
    return date_obj.weekday()==5 or date_obj.weekday()==6

def get_time_range(date_obj):
    if date_obj.hour>=7 and date_obj.hour<=10:
        return "7-10"

    if date_obj.hour>10 and date_obj.hour<=12:
        return "10-12"

    if date_obj.hour>12 and date_obj.hour<=17:
        return "12-17"

    if date_obj.hour>17 and date_obj.hour<=20:
        return "17-20"

    if date_obj.hour>20 and date_obj.hour<=22:
        return "20-22"

    if date_obj.hour>22:
        return "22-24"

    return "00-7"


def get_distance_range(trip_distance):
      if trip_distance>= 0.00 and trip_distance <=3.00:
        return  "0-3"
      elif trip_distance>= 3.01 and trip_distance <=6.00:
        return  "3-6"
      elif trip_distance>= 6.01 and trip_distance <=9.00:
        return  "6-9"
      elif trip_distance>= 9.01 and trip_distance <=12.00:
        return  "9-12"
      elif trip_distance>= 12.01 and trip_distance <=15.00:
        return  "12-15"
      elif trip_distance>= 15.01 and trip_distance <=18.00:
        return  "15-18"
      elif trip_distance>= 18.01 and trip_distance <=21.00:
        return  "18-21"
      elif trip_distance>= 21.01 and trip_distance <=24.00:
        return  "21-24"
      elif trip_distance>= 24.00:
        return  "24-infinite"


for line in sys.stdin:
    data = line.strip().split(",")

    if len(data)< 18 or data[0]=="vendor_id" or data[0]=="VendorID":
        continue

    pickup_date_time = data[1]
    trip_distance = float(data[4])
    fare_amount = data[12]
    dropoff_time = data[2]

    date_obj = convert_str_to_date(pickup_date_time)
    date_obj_drop_off = convert_str_to_date(dropoff_time)
    dist_range = get_distance_range(trip_distance)
    result = "weekend" if is_weekend(date_obj) else "weekday"
    time_range = get_time_range(date_obj)
    trip_seconds = (date_obj_drop_off - date_obj).seconds
    print str(result) + "," + str(time_range) + "," + str(dist_range) + "\t" + str(fare_amount) + ","+str(trip_seconds)
