#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:41:51 2023

@author: ml
"""
def hex_to_dec():
    dec_num = 0
    
    hex_num = input('輸入十六進位數字：')
    
    #method 1:
    #reversed():反轉字串，讓位數的次方數與該次方數字對應
    #2A => 2:1次方 A:0次方 => 反轉後A2方便迭代時運算
    #enumerate():同時取得索引與元素
    '''for power, num in enumerate(reversed(hex_num)):
        #如果字元是0~9直接轉換
        if num.isdigit():
            num = int(num)
        #如果字元是A~F,用ASCII轉換為10~15
        else:
            num = ord(num.upper()) - ord('A') + 10
            
        #16位轉10進位算法(走訪每個位數，將數字乘以16的第n位數次方)
        dec_num += (16 ** power) * num'''
        
    #method2:
    #用int轉換不同進位數，第二個參數表示前面的字串是幾進位
    dec_num = int(hex_num, 16)
    
    print('十位數結果：', dec_num)


hex_to_dec()