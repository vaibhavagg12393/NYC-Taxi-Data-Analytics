#!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) < 18 or data[0] == "vendor_id" or data[0] == "VendorID":
        continue

    passenger_count = data[3]

    print(str(1)+ "\t" + passenger_count)

