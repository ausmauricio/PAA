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
    
    for i in xrange(v-1):

        k = i

        for j in xrange(v-1-k):

            k = k + 1
            print(str(i) + "," + str(k))

print("0,0")
