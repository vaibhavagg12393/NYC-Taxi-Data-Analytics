#!/usr/bin/env python
import sys
import datetime
import json
import matplotlib
from matplotlib.path import Path
from shapely.geometry import Point,shape
from rtree import index
import numpy
sys.path.append(".")

def is_valid_area(area):
    if len(area)<2:
        return False
    if area[0]==0 or area[1]==0:
        return False
    return True

def find_neighborhood(area,rtree_index,neighborhoods):
    if is_valid_area(area):
        point = Point(area[0],area[1])
        match = rtree_index.intersection((area[0],area[1],area[0],area[1]))
        for m in match:
            if neighborhoods[m][2].contains(point):
                return m
    return -1

def filter_coords(c):
    a = []
    for x,y in c[0]:
        a.append((y,x))
    return [a]

def makeIndex(neighborhoods, geo_values, rtree_index):
    for geo_value in geo_values:
        paths = map(Path,geo_value['geometry']['coordinates'])
        bounding_box = paths[0].get_extents()
        map(bounding_box.update_from_path, paths[1:])
        rtree_index.insert(len(neighborhoods),list(bounding_box.get_points()[0])+list(bounding_box.get_points()[1]))
        neighborhoods.append((geo_value['properties']['borough'],geo_value['properties']['neighborhood'],shape(geo_value['geometry'])))
    neighborhoods.append(('NA','NA',None))

with open('pediacitiesnycneighborhoods.geojson') as geo_data_file:
    geo_data = json.load(geo_data_file)
neighborhoods = []
rtreeIndex = index.Index()
makeIndex(neighborhoods,geo_data['features'],rtreeIndex)

for line in sys.stdin:
    line = line.strip()
    values = line.split(",")
    if len(values)<18 or values[0]=="vendor_id" or values[0]=="VendorID":
        continue
    try:
        drop_off_lat = float(values[10])
        drop_off_long = float(values[9])
        pick_up_lat = float(values[6])
        pick_up_long = float(values[5])

        pick_up_index = find_neighborhood((pick_up_long,pick_up_lat),rtreeIndex,neighborhoods)
        drop_off_index = find_neighborhood((drop_off_long,drop_off_lat),rtreeIndex,neighborhoods)
        print line+"\t"+str(neighborhoods[pick_up_index][0])+","+str(neighborhoods[pick_up_index][1]+","+str(neighborhoods[drop_off_index][0]+","+str(neighborhoods[drop_off_index][1])))
    except Exception:
        pass
