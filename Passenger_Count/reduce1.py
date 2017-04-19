#!/usr/bin/env python
import sys
total_passengers = 0
for line in sys.stdin:
    key, value = line.strip().split("\t")
    total_passengers += int(value)
avg_passengers = float(total_passengers) / 365
print(str(avg_passengers) + "\t"+ str(total_passengers))