#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:20:52 2023

@author: ml
"""
def pig_latin(input_str):
    
    #input_str = input('請輸入一個英文單字：')
    
    head_char = input_str[0]
    
    #字串為容器，可像list般走訪
    #in 檢查字元是否存在於字串中
    #f-string字串格式化 {}變數名稱會拿變數的值填入，運算式則會顯示計算後的值
    if head_char in 'aeiou':
        #return input_str + 'way'
        return f'{input_str}way'
    else:
        #切片 字串[起始索引：終點索引(不含)]
        #return input_str[1:] + head_char + 'ay'
        return f'{input_str[1:]}{head_char}ay'
        
    #字串為不可變的，當修改字串，其實是產生新字串
    '''word = 'python'
    print(id(word))
    word = word+' Workout'
    print(id(word))'''
        
    
#pig_latin()