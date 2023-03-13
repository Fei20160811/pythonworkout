#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:10:17 2023

@author: ml
"""
def dict_diff(dict1, dict2):
    
    diff_dic = {}
    
    #兩個dict的最大不重複鍵值
    #dict_keys()傳回的dict_keys型別容器，和setㄧ樣適用聯集(|)、差集(-)、交集(&)、對稱差集(^)
    all_keys = sorted(dict1.keys() | dict2.keys())
    
    #逐一抓取對應資料比對，有差異者寫入相異dict
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        
        if value1 != value2:
            diff_dic[key] = [value1, value2]
   
    return diff_dic
    

dict1 = {'a':1, 'b':2, 'c':3, 'd':5}
dict2 = {'a':1, 'b':2, 'd':4, 'e':6}

print(dict_diff(dict1, dict2))

    