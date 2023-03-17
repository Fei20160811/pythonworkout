#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:37:08 2023

@author: ml
"""
import string

def gematria_dict():
        
    #使用string.ascii_lowercase 取得英文字母清單
    for index, char in enumerate(string.ascii_lowercase):
        #使用enumerate傳回上述字母與其對應數字
        #指定enumerate第二個參數為1，讓索引從1開始計
        return { char:index for index, char in enumerate(string.ascii_lowercase, 1) }
    
    
GEMATRIA = gematria_dict()

def gematria_value(word):
    #lower()確保將單字轉小寫
    #需加入判斷該字元是否為字母，如果是的話才加入計算
    return sum([GEMATRIA.get(char) for char in word.lower() if char in GEMATRIA])

#print(gematria_value('apple'))


def gematria_equal_words(compare_word, file_path):
    
    baseNum = gematria_value(compare_word)
    
    #用UTF-8開啟檔案
    with open(file_path, encoding='utf-8') as file:
        #lower()確保將單字轉小寫
        return [ word for line in file for word in line.lower().split() if gematria_value(word) == baseNum]

print(gematria_equal_words('apple', r'./sample/pg11.txt'))
    

print(gematria_value('damages'))
    