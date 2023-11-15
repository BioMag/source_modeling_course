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
""" Powerful iterating tools allow some cool stuff
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


#%%
""" Dictionaries
"""

#%% Cell #6
""" Dictionaries are all about key:value pairs
"""
consts = {'e' : 2.7183, 'pi' : 3.1416, 'golden ratio' : 1.618}
print(consts.keys())


#%% Cell 7
""" You can index dictionaries using keys -- this is similar to indexing arrays
    using integers
"""
print(consts['pi'])
consts['pi'] = 3.2     # For those in Indiana, USA
print(consts['pi'])


#%% Cell 8
""" Use .keys() method to get a list of keys for an object
"""
consts.keys()



