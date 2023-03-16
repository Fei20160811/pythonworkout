#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:56:09 2023

@author: ml
"""
def sum_numbers(input_str):
    #method1
    #生成式的if過濾條件
    #[ 值或運算式 for 值 in 容器 if 條件判斷式]
    #isnumeric() v.s is.digit()
    return sum([int(num) for num in input_str.split(' ') if num.isdigit()])

    #method2
    '''
    #map() & filter() & lambda
    #filter(函式, 容器)
    return sum(list(map(int, filter(lambda num:num.isdigit(), input_str.split()))))'''

print(sum_numbers('10 abc 20 de44 30 50fg 40'))