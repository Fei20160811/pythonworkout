#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:02:02 2023

@author: ml
"""
def zeroes_to_the_end(data):
    #method1
    '''
    #增刪法
    #data.coumt(0) => 有幾0就走訪幾次
    for _ in range(data.count(0)):
        #將前面的0刪掉
        del data[data.index(0)]
        #結尾再增加0
        data.append(0)
    return data'''

    #切片法
    for _ in range(data.count(0)):
        idx = data.index(0)
        data = data[:idx] + data[idx+1:] + data[idx:idx+1]
    return data

print(zeroes_to_the_end([2,3,0,1,0,5]))
            
        
            