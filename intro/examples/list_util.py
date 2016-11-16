#!/usr/bin/env python

from math import *
import sys

def appliquer(l,f):
    for x in l:
        print "{0} -> {1}".format(x,f(x))

def image(l, f):
    return [ f(x) for x in l]

def somme(l):
    acc = 0.0
    for x in l:
        acc = acc + x
    return acc

def moyenne(l):
    sz = len(l)
    if sz == 0:
        return 0
    else:
        return somme(l)/sz

def quadratic(l):
    return sqrt(moyenne([x**2 for x in l]))

if __name__ == '__main__':
    if abs(quadratic([2]) - 2) > 0.00001:
        print "Problem"
        sys.exit(-1)
    else:
        print "OK"
        sys.exit(0)

