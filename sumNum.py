#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:10:52 2023

@author: ml
"""

#資料檢查？？？
#func(*args) => 定義接收數量不定的參數
#start 加總的初始值
def my_sum(*numbers, start=0):
       
    #計算加總
    total = 0

    for num in numbers:
        total += num
   
    return total+start
        
    
print(my_sum(1,2,3,4,5, start=10))
print(my_sum(1,2,3,4,5.5))