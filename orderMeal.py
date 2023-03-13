#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:29:59 2023

@author: ml
"""
import time

def order_meal():
    meal_dic = { 
        '三明治':50,
        '咖啡':40,
        '沙拉':30
        }
    
    total = 0
    
    while meal := input('請點餐：'):
        
        #使用dic.get(key)方法較安全，如果有找到該key則回傳對應的value，如果沒有找到key則回傳None，不會造成程式錯誤
        #method1 suggestion
        price = meal_dic.get(meal)
        
        if price:
            total += price
            print(f'{meal} {price}元，總金額：{total}')   
        else:
            print(f'抱歉！我們沒有供應{meal}')
        
        
        #method2
        #如果使用dic[key]取值，如果沒找到key會造成keyError的錯誤(須先使用in判斷key是否存在於dic中)
        '''if meal in meal_dic:
            price = meal_dic[meal]
            total += price
            print(f'{meal} {price}元，總金額：{total}')
        else:
            now = time.time()
            print(f'抱歉！我們沒有供應{meal}')'''
            
        
    
    return f'您的帳單為 {total} 元'


print(order_meal())