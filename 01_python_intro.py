#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A brief Python primer (with an emphasis on differences with MATLAB).
"""


#%% Cell #0 
""" Welcome to Python! This is a Python cell. Python is interactive and
    REPL-friendly
"""
print("Hello world!")    # "Hello world!" example is mandatory!

    
#%% Cell #1
""" Python is 0-based
"""
lst = ['a', 'b', 'c']
print(lst[0])
print(lst[2])


#%% Cell #2
""" Python is 0-based
"""
for i in range(10):
    print(i)
   

#%% Cell #3
""" Python parses indentation!
"""
cnt0 = 0
cnt1 = 0

for i in range(10):
    for j in range(10):
        cnt0 += 1
    cnt1 += 1
    
print('cnt0 = %i' % cnt0)
print('cnt1 = %i' % cnt1)


#%% Cell #4
""" [] are for indexing, () are for function calls
"""
lst = ['a', 'b', 'c']

func = abs(-1)
indx = lst[-1]

print(func)
print(indx)


#%% Cell #5
""" Things are sometimes passed by value ...
"""
var0 = 1
var1 = var0

var1 = 2
print(var0)
print(var1)


#%% Cell #6
""" ... and sometimes by reference (although some people will argue that
    there is no such thing as "by-value" in Python).
    For more, read on mutable vs immutable data type
"""
var0 = ['a', 'b', 'c']
var1 = var0

var0[1] = 'd'
print(var0)
print(var1)


#%% Cell #7
""" You need to import things before you can use them
"""
from math import sqrt
print(sqrt(4))


#%% Cell #8
""" You need to import things before you can use them
"""
import numpy as np
print(np.eye(3))


