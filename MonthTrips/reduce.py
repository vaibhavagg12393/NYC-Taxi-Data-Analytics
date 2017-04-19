#!/usr/bin/env python
import sys
previous_key = None
total = 0
for line in sys.stdin:
    key, value = line.split("\t")
    if not previous_key or previous_key == key:
        total += int(value)
    else:
        print previous_key+"\t"+str(total)
        total = int(value)
    previous_key = key
if previous_key:
    print previous_key+"\t"+str(total)
