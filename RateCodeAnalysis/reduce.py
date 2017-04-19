#!/usr/bin/env python
import sys
previous_key = None
num_trips = 0.0
std_rate = 0.0
jfk = 0.0
newark = 0.0
nw = 0.0
negotiated = 0.0
grp_ride = 0.0
total = 0.0

for line in sys.stdin:
	key, value = line.strip().split("\t")
	rate_code = int(value)
	if not previous_key or previous_key == key:
		if rate_code ==  1:
			std_rate +=1
		elif rate_code == 2:
			jfk +=1
		elif rate_code == 3:
			newark +=1
		elif rate_code == 4:
			nw +=1
		elif rate_code == 5:
			negotiated +=1
		elif rate_code == 6:
			grp_ride +=1
	else:
		total = std_rate+jfk+newark+nw+negotiated+grp_ride
		std_rate_p = (std_rate/total)*100
		jfk_p = (jfk/total)*100
		newark_p = (newark/total)*100
		nw_p = (nw/total)*100
		negotiated_p = (negotiated/total)*100
		grp_ride_p = (grp_ride/total)*100
		print previous_key +","+ str(std_rate_p)+ "," + str(jfk_p)\
				+ "," + str(newark_p) + "," + str(nw_p) + "," + str(negotiated_p)\
				+ "," + str(grp_ride_p)

		std_rate = 0.0
		jfk = 0.0
		newark = 0.0
		nw = 0.0
		negotiated = 0.0
		grp_ride = 0.0
		total = 0.0
		rate_code = int(value)
		if rate_code ==  1:
			std_rate +=1
		elif rate_code == 2:
			jfk +=1
		elif rate_code == 3:
			newark +=1
		elif rate_code == 4:
			nw +=1
		elif rate_code == 5:
			negotiated +=1
		elif rate_code == 6:
			grp_ride +=1
	previous_key = key
if previous_key:
	total = std_rate+jfk+newark+nw+negotiated+grp_ride
	std_rate_p = (std_rate/total)*100
	jfk_p = (jfk/total)*100
	newark_p = (newark/total)*100
	nw_p = (nw/total)*100
	negotiated_p = (negotiated/total)*100
	grp_ride_p = (grp_ride/total)*100

	print previous_key + ","+ str(std_rate_p)+ "," + str(jfk_p)\
		+ "," + str(newark_p) + "," + str(nw_p) + "," + str(negotiated_p)\
		+ "," + str(grp_ride_p)
