# -*- coding: utf-8 -*-

from random import randint
import sys

# you should read create_dense_graph.py first.
# this will randomly select some edges to be excluded
# from the dense graph and therefore create a sparse graph.
# we use the randint function to generate a number
# and use it to cut the graph.
# if you want to cut 70% of the edges of the dense graph
# for example, than you should probable make a < 30
# and hopefully it will be close.

if int(sys.argv[1]) == 1:

    v = int(sys.argv[2])
    
    for i in xrange(v-1):
        k = i
        for j in xrange(v-1-k):
        
            k = k + 1
            a = randint(1,100)
            
            if a < 60:
                print(str(i) + "," + str(k) + "," + str(a))
            
