#!/usr/bin/env python
import sys

if __name__ == "__main__":
  for line in sys.stdin:
    a = line.split(",")
    sys.stdout.write("{0}\t{1}\n".format(a[3],a[6])) #Print Origin Airport and Departure Delay in Minutes
