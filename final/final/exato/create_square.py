# -*- coding: utf-8 -*-

import sys

size = int(sys.argv[1]) # size x size

k = 0

for i in xrange(size * (size-1)):

    if i%size == (size-1):

        print(str(k) + "," + str(k + size))

    else:

        print(str(k) + "," + str(k + 1))
        print(str(k) + "," + str(k + size))
    
    k += 1

for j in xrange(size - 1):

    print(str(k) + "," + str(k + 1))
    k += 1

print("0,0")
