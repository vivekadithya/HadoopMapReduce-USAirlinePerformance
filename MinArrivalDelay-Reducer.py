#!/usr/bin/env python
import sys

current_key = None
a = []
for line in sys.stdin:
    key, val = line.split("\t")
    if val != 'ARR_DELAY' and val is not None:
        val = val.strip()
        try:
            val = float(val)
        except:
            continue
        if key == current_key:
            a.append(val)
        elif current_key is not None:
            sys.stdout.write("{0}\t{1}\n".format(current_key, min(a)))
            a[:]=[]
        current_key = key
        a.append(val)
if current_key: #ensure the last key is written out
    sys.stdout.write("{0}\t{1}\n".format(current_key, min(a)))
