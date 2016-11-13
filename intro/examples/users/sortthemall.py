#!/usr/bin/env python

import argparse
import sys
from datetime import date

argparser = argparse.ArgumentParser(description="User list sorting program.")
argparser.add_argument('-s','--sortby', metavar='OUPUT', type=str, choices=['name', 'age'],
                       help='The sort criteria.', default='name')

simple_arg_parsing = True
if (simple_arg_parsing):
    argparser.add_argument('-i','--input', metavar='INPUT', type=str, nargs=1,
                           help='The input file.')
    argparser.add_argument('-o','--output', metavar='OUPUT', type=str, nargs=1,
                           help='The output file.')
    parsedargs = argparser.parse_args()
    if parsedargs.input:
        ifile = open(parsedargs.input[0], 'r')
    else:
        ifile = sys.stdin
    if parsedargs.output:
        ofile = open(parsedargs.output[0], 'r')
    else:
        ofile = sys.stdout
else:
    argparser.add_argument('input', nargs='?', type=argparse.FileType('r'),
                           default=sys.stdin)
    argparser.add_argument('output', nargs='?', type=argparse.FileType('w'),
                           default=sys.stdout)
    parsedargs = argparser.parse_args()
    ifile = parsedargs.input
    ofile = parsedargs.output

users = []
for l in ifile:
    try:
        lastname, firstname, bithdate, desc = l.rstrip().split(";")
        users.append((firstname.strip(), lastname.strip(), bithdate.strip(), desc.strip()))
    except:
        print "couldt deal with '",l,"'"

def str2date(s):
    day, month, year = s.split("/")
    return date(int(year), int(month), int(day))

def cmp_birthdate(u1, u2):
    b1 = str2date(u1[2])
    b2 = str2date(u2[2])
    if b1 < b2:
        return 1
    elif b2 < b1:
        return -1
    else:
        return 0

if (parsedargs.sortby == 'age'):
    users.sort(cmp=cmp_birthdate)
    # or: users.sort(cmp=lambda u1, u2: int((str2date(u2[2]) - str2date(u1[2])).total_seconds()))
elif (parsedargs.sortby == 'name'):
    users.sort(key=lambda u: u[1])

for i,u in enumerate(users):
    print "{0}: {1}".format(i, repr(u))

