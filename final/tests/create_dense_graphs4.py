# -*- coding: utf-8 -*-

import sys

# 1: dense
# 2: sparse

# doesn't actually create sparse graph tho.
# the edge weights will be between 1 and 100.
# this script creates a text file containing all 
# v(v-1)/2 possible edges given a vertice number.

if int(sys.argv[1]) == 1:

    v = int(sys.argv[2]) # number of vertices

    for i in xrange(1,v):
        k = i
        for j in xrange(v-1-k):
            k = k + 1
            print(str(i) + "," + str(k))
    
    for i in xrange(1, v):
        print("100000," + str(i))    

    print("100000,200000")

    for i in xrange(v + 1, 2*v):
        k = i
        for j in xrange(2*v-1-k):
            k = k + 1
            print(str(i) + "," + str(k))

    for i in xrange(v + 1, 2*v):
        print("200000," + str(i))

    for i in xrange(1,v):
        print(str(i) + "," + str(2*v - i))

print("0,0")
