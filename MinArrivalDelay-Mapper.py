#!/usr/bin/env python
import sys

if __name__ == "__main__":
for line in sys.stdin:
a = line.split(",")
sys.stdout.write("{0}{1}\t{2}\n".format(a[3],a[4],a[8]))
