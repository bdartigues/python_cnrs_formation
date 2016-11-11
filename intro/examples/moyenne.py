#!/usr/bin/env python

import sys

def moyenne(a,b):
    m = (a+b)/2
    return m

if (len(sys.argv) != 3):
    print "Usage: {0} <a> <b>".format(sys.argv[0])
else:
    a, b = float(sys.argv[1]), float(sys.argv[2])
    print "Moyenne de {0} et {1}: {2}".format(a,b,moyenne(a,b))

