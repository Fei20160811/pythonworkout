#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:10:52 2023

@author: ml
"""

#資料檢查？？？
#func(*args) => 定義接收數量不定的參數 seq_obj型態為tuple
#start 加總的初始值
def my_sum(*seq_obj, start=0):
       
    #version 1:
    #計算加總
    '''total = 0

    for num in seq_obj:
        total += num
   
    return total+start'''

    #version2:
    #處理不同型別資料
    #判斷是否有傳入值
    if not seq_obj:
        return seq_obj
    
    #取出輸入值的第一筆資料，作為後續資料的型態處理依據
    result = seq_obj[0]
    
    #第一筆已經取出，所以從第二筆開始跑迴圈
    for item in seq_obj[1:]:
        #判斷傳入值是否為dict
        if isinstance(item, dict):
            result.update(item)
            #result |= item #pytno3.9
        else:
            result += item
    
    return result
    
    
print(my_sum(1,2,3,4,5, start=10))

print(my_sum())
print(my_sum(10,20,30,40,50.5))
#字串與list or tuple 元素會相連
print(my_sum('abc', 'd', 'e'))
print(my_sum([10, 20, 30], [40, 50], [60]))
#若併入的dict含有相同的key，新的會蓋過舊的
print(my_sum({'A':1, 'B':2}, {'B':4, 'C':3}))