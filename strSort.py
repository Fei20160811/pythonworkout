#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:12:53 2023

@author: ml
"""
def strsort():
    input_str = input('請輸入需要排序的字串：')
    
    #method1
    '''l = list(input_str)
    #sort()直接在原list排序，所以沒有回傳值
    l.sort() 
    print(('').join(l))'''
    
    #method2
    #sorted() 複製原list進行排序，回傳新list
    #加入第二個參數(key=str.lower)，如果字串有大小寫，將大寫轉小寫後排序，但回傳字串不改變大小寫
    print(('').join(sorted(input_str, key=str.lower)))
    
strsort()