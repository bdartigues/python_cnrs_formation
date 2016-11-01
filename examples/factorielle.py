#!/usr/bin/env python

import sys

def fac(n):
    if (n == 1):
        return 1
    else:
        return n*fac(n-1)

if (len(sys.argv) != 2):
    print "Usage: {0} <N>".format(sys.argv[0])
else:
    print fac(int(sys.argv[1]))
