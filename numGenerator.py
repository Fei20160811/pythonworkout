#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:44:38 2023

@author: ml
"""
def num_generator(data):
    #我的答案
    #return (num for num in str(data).replace('.',''))
    #產生器運算式(值或運算式 for 值 in 容器 if 條件判斷式)
    return (int(digit) for digit in str(data) if digit.isnumeric())
        
        
nums = num_generator(3.14159)
print(nums)
for num in nums:
    print(num)