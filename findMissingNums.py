#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:04:27 2023

@author: ml
"""
def find_missing_nums(data):
    #我的答案
    '''
    missing_list = []
    for index in range(1, len(data)+1):
        if index not in set(data):
            missing_list.append(index)
    return missing_list'''
    
    #差集解法
    all_data = set(range(1, len(data)+1))
    return list(all_data - set(data))
            
print(find_missing_nums([1, 2, 8, 5, 1, 6, 4, 9, 5]))