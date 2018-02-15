#!/bin/bash

in=$1

python2 mcds.py sparse/$in 1 > out1
python2 mcds.py sparse/$in 2 > out2
python2 mcds.py sparse/$in 3 > out3
