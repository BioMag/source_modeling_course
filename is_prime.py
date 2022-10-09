#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:01:46 2022

@author: andrey
"""
import math

def isprime(num):
    """
    Return True if num is prime and False otherwise

    """
    div = 2
    while div <= math.sqrt(num):
        if num % div == 0:
            return False
        div += 1
    return True


print(isprime(15))
print(isprime(7))