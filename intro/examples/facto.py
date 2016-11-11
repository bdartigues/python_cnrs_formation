#!/usr/bin/env python

def fac(n):
    if (n == 1):
        return 1
    else:
        return n*fac(n-1)

if (__name__ == '__main__'):
    import sys
    if (len(sys.argv) == 2):
        print fac(int(sys.argv[1]))
    elif (len(sys.argv) == 1):
        if (fac(1) == 1 and fac(3) == 6):
            print "la fonction fac passe les tests."
            sys.exit(0)
        else:
            print "la fonction fac a un soucis."
            sys.exit(-1)
            
    else:
        print "Usage: {0} [<N>]".format(sys.argv[0])
        sys.exit(1)
        


