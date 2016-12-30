#!/usr/bin/env python
import sys

if __name__ == "__main__":
  for line in sys.stdin:
    a = line.split(",")
    sys.stdout.write("{0}\t{1}\n".format(a[2],a[8])) #Print Flight Number and Arrival Delay
