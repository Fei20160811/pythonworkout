#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:55:49 2023

@author: ml
"""
def reverse_binary(data):
    #用字串格式化將整數轉成8位元的二進位數
    #08b => 有8字元長度，不滿8位時在開頭補0，而且是2進位
    #亦可寫做‘{:08b}'.format(data)
    binary = f'{data:08b}'
    #用切片方式反轉字串
    #把字串的2進位轉為10進位數
    return int(binary[::-1], 2)

    
print(reverse_binary(121))