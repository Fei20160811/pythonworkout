#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:04:42 2023

@author: ml
"""

def word_generator(file_path, max_length):
    
    #我的答案 => 全讀出再取所需單字數量，可能會有效能問題
    '''
    with open(file_path, encoding='UTF-8') as file:
        word_list = [word for line in file for word in line.split()]
        for index in range(max_length):
            yield word_list[index]
    '''
    with open(file_path) as file:
        index = 0
        for line in file:
            for word in line.split():
                if index >= max_length:
                    return
                #產生器函式使用yield回傳值，會繼續保留在記憶體中，下次呼叫時就會從上次執行yield的地方繼續，直到走訪結束
                yield word.replace('.','')
                index += 1
        
     
ten_words = word_generator(r'./sample/text2.txt', 10)
#收到產生器物件
print(ten_words)
#可透過__next__()取值
print(ten_words.__next__())
print(ten_words.__next__())
#for word in ten_words:
#    print(word)
