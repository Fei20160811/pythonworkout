#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:27:53 2023

@author: ml
"""
def find_common_prefix(data):
    
    common_prefix = []
    
    #使用zip走訪多重容器
    #*data解包
    #我的答案
    '''
    for c1, c2, c3 in zip(*data):
        if c1 == c2 and c2 == c3:
            common_prefix.append(c1)
        else:
            break'''
            
    for c in zip(*data):
        #將每個單字字元丟進set，如果只剩一個字表示全部相同
        if len(set(c)) == 1:
            common_prefix.append(c[0])
        else:
            break
    
    return ''.join(common_prefix)


print(find_common_prefix(['expensive', 'export', 'experience']))
print(find_common_prefix(['flight', 'flower', 'book']))