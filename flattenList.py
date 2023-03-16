#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:11:12 2023

@author: ml
"""
def flatten(data):
    #巢狀走訪生成式     
    return [sub_element for element in data 
                   for sub_element in element]

print(flatten([[1,2],[3,4]]))