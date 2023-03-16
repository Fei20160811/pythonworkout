#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:47:13 2023

@author: ml
"""
def abs_numbers(abs_list):
    #method1
    '''
    #list生成式
    #[ 值或運算式 for 值 in 容器 ] => 從容器取值，然後直接輸出值，或者對值做任意運算
    return [abs(num) for num in abs_list]'''

    #method2
    #map()
    #將容器的每個元素套進其函數參數，並將函式結果包成map容器傳回(通常得自己再自行轉型)
    return list(map(abs, abs_list))

print(abs_numbers([1, -2, 3, -4, 5]))