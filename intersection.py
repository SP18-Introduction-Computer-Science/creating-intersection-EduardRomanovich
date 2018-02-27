# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:55:42 2018

@author: emrom
"""

a = [1,4,5,7,8,12]
b = [4,5,9,12,15,2]
c = (intersection(a,b))
def intersection(a, b):
    c = [value for value in a if value in b]
    return c
print(c)
