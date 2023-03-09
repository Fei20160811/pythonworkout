#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:55:04 2023

@author: ml
"""

import codecs

def rot13():
    #如果使用字串累加的方式產生新字串，當處理大量資料時會造成效能與記憶體用量問題
    rot_word = []
    
    input_word = input('請輸入需要加密的單字：')
    
    #method1
    '''for char in input_word.lower():
        #往後算第13個字母
        ord_num = ord(char) + 13
        #檢查移動後是否超過z，是的話就回減26，從a算起
        if ord_num > ord('z'):
            ord_num -= 26
            
        rot_word.append(chr(ord_num))
    
    print(''.join(rot_word))'''
    
    #method2
    #使用內建的rot13加密法 codecs.encode
    print(codecs.encode(input_word, 'rot_13'))

    
rot13()