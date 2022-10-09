#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The basics of Python.
"""


# %% Cell #0
""" Let's define a function!
"""
def pow2(inp):
    return(inp*inp)

print(pow2(3))


# %%
""" Lists and tuples
"""


# %% Cell #1
""" Lists and tuples can be indexed
"""
my_list = ['a', 'b', 1]
my_tuple = ('a', 'b', 1)

print(my_list[1])
print(my_tuple[1])


# %% Cell #2
""" Lists can also be changed
"""
my_list[1] = 5
print(my_list)


# %% Cell #3
""" Lists, tuples, and many other things can be iterated over
"""
my_list = ['a', 'b', 'c']

for c in my_list:
    print(c)


# %%
""" Powerfool iterating tools allow some cool stuff
"""


# %% Cell #4
""" Concatenate two lists of strings, memberwise. The classic way ...
"""

strs0 = ['a', 'b', 'c']
strs1 = ['x', 'y', 'z']

res = []

for i in range(len(strs0)):
    res.append(strs0[i] + strs1[i])

print(res)


# %% Cell #5
""" ... and the cool pythonic way
"""
strs0 = ['a', 'b', 'c']
strs1 = ['x', 'y', 'z']

res = [s0 + s1 for (s0, s1) in zip(strs0, strs1)]

print(res)
