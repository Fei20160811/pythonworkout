#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:15:35 2023

@author: ml
"""
class strDict(dict):
        
    def __setitem__(self, k, v):
       dict.__setitem__(self, str(k), v)
        
    def __getitem__(self, k):
       if str(k) not in self:
           self[k] = None
       return dict.__getitem__(self, str(k))
        
        
sd = strDict()
sd[1] = 1
sd[3.14] = 3.14 
sd['10'] = 'test'

print(sd[1])
print(sd['3.14'])
print(sd[10])
print(sd['a'])

print(sd)