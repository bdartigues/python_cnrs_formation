#!/usr/bin/env python

import sys

# Compute the factorial n! of a positive integer.
# Can easilly overflow
def fac(n):
    if (n == 1): # if n is 1, return 1 //  BAD
        return 1
    else:
        return n*fac(n-1)

if (len(sys.argv) != 2):
    print "Usage: {0} <N>".format(sys.argv[0])
else:
    print fac(int(sys.argv[1]))
