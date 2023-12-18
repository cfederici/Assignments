#!/usr/bin/env python3

#Author: Chris Federici
#Author ID: cfederici
#Date Created 2023/09/11

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
