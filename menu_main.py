#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:23:19 2023

@author: ml
"""
#一般 python menu.py可執行，但spyder會出錯
#從自訂的menu模組匯入menu()
from menu import menu

#各種外部函式
def func_a():
    return '執行函式A'

def func_b():
    return '執行函式B'

def func_x():
    return '執行函式X'

#建立menu物件
my_menu = menu(a=func_a, b=func_b, x=func_x)

#傳回使用者所選擇的外部函式
func = my_menu()
#執行外部函式
print(func())
