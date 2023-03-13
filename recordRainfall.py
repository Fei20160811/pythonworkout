#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:14:26 2023

@author: ml
"""
from collections import defaultdict

def record_rainfall():
    
    #method1 
    #需先檢查dic是否有該值，才進行後續運算
    '''rainfall_dic = {}
    
    while city := input('輸入城市：'):       
        if not (rain_mm := input('輸入雨量(mm):')):
            rain_mm = 0
        
        #dic[key]=value，如果key不存在，建立新key並存入該值，如key存在覆寫原本的值
        #dict.get(key)在查無key值資料時，傳回預設值
        rainfall_dic[city] = rainfall_dic.get(city, 0) + int(rain_mm)'''
        
    #method2
    #使用defaultdict，能夠在查無此鍵時自動新增並指派預設值
    #defaultdict(int) 建立新鍵時使用int()的傳回值0
    rainfall_dic = defaultdict(int)
    
    while city := input('輸入城市：'):
        if not (rain_mm := input('輸入雨量(mm):')):
            rain_mm = 0
        
        rainfall_dic[city] += int(rain_mm)
    
    #使用dic.items()取得元素的key & value
    for key, value in rainfall_dic.items():
        print(f'{key}: {value} mm')
        
record_rainfall()