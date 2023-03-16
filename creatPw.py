#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:24:50 2023

@author: ml
"""

import random

def set_password_source(source):
    
    #閉包函式:當一個函式的回傳值是它內部定義的子函式，此子函式又使用父函式的變數時，子函式稱之為閉包
    #閉包函式，會記住變數source
    def my_pw_gen(length):
        
        pw_list = []
        
        for i in range(length):
            #random.choice() 從容器中隨機挑選元素
            #從source隨機挑length個字元放進pw_list中
            pw_list.append(random.choice(source))
        
        return ''.join(pw_list)
    
    #傳回密碼產生器的閉包函式
    return my_pw_gen

#設定密碼產生器的來源字串，設定自訂密碼產生函式
my_pw_gen = set_password_source('0123456789abcdefghij')
#呼叫自訂密碼函式，產生10位數密碼
print(my_pw_gen(10)) 
