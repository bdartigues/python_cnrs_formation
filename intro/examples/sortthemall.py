#!/usr/bin/env python

import argparse
import sys

argparser = argparse.ArgumentParser(description="User list sorting program.")

simple_arg_parsing = True
if (simple_arg_parsing):
    arparser.add_argument('-i','--input', metavar='INPUT', type=str, nargs=1,
                          help='The input file.')
    arparser.add_argument('-o','--output', metavar='OUPUT', type=str, nargs=1,
                          help='The output file.')
    print argparser.parse_arg(sys.argv)
else:
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)
    print argparser.parse_arg(sys.argv)

