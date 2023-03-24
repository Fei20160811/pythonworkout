#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:24:16 2023

@author: ml
"""
def sum_of_two(data, num):
    #method1 雙層for迴圈
    '''
    for index_a, value_a in enumerate(data):
        for index_b, value_b in enumerate(data):
            #索引不同但相加結果相同
            if index_a != index_b and (value_a + value_b == num):
                return [index_a, index_b]
    #沒有找到結果，回傳空陣列
    return []'''
    
    #method2 使用itertools
    from itertools import combinations
    
    #combinations(data, k) 列出不重複元素，以k為一組
    for a, b in combinations(enumerate(data), 2):
        if a[1] + b[1] == num:
            return [a[0], b[0]]
    return []
            
print(sum_of_two([3 ,5 , 9, 6], 8))
print(sum_of_two([3 ,2 , 2], 4))
print(sum_of_two([3 ,7 , 8], 9))