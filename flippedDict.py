#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:04:00 2023

@author: ml
"""
def flipped_dict(data):
    
    #method1 
    #dict生成式
    #return { value:key for key, value in data.items()}
    
    #method2
    #只走訪dict鍵的dict生成式
    return { data.get(key):key for key in data }

print(flipped_dict({'a':1, 'b':2, 'c':3}))