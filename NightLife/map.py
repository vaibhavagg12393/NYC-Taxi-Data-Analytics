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

popular_place_month = {}

for line in sys.stdin:
    line = line.strip()
    if "\t" not in line:
        continue
    key,value = line.strip().split('\t')
    data = key.split(",")
    area_data = value.split(",")
    if len(area_data)<4 or area_data[1].strip()=="" or area_data[1].strip()=="NA"\
    or area_data[3].strip()=="" or area_data[3].strip()=="NA":
        continue
    if len(data)<18 or data[0]=='vendor_id' or data[0] == "VendorID":
        continue
    pick_up_date_obj = convert_str_to_date(data[1])
    drop_off_date_obj = convert_str_to_date(data[2])
    if (drop_off_date_obj.weekday()==4 and drop_off_date_obj.hour>=21)\
        or (drop_off_date_obj.weekday()==5 and (drop_off_date_obj.hour>=21 or drop_off_date_obj.hour<=1))\
        or (drop_off_date_obj.weekday()==6 and drop_off_date_obj.hour<=1):
            inner_key = str(drop_off_date_obj.month)+","+area_data[3]+","+area_data[2]
            if popular_place_month.get(inner_key):
                popular_place_month[inner_key]+=1
            else:
                popular_place_month[inner_key]=1
    elif (pick_up_date_obj.weekday()==5 or pick_up_date_obj.weekday()==6) and pick_up_date_obj.hour<=4:
            inner_key = str(drop_off_date_obj.month)+","+area_data[1]+","+area_data[0]
            if popular_place_month.get(inner_key):
                popular_place_month[inner_key]+=1
            else:
                popular_place_month[inner_key]=1
for key in popular_place_month:
    print str(key)+"\t"+str(popular_place_month[key])
