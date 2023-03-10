#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 18:06:31 2023

@author: ml
"""

from collections import Counter

def most_repeated_letter(str_seq):
    
    #method1 
    #使用count()
    letter_list = []
    
    #set() 取得字串不重複的字母
    '''letters = set(str_seq)
    
    for letter in letters:
        #count() 計算元素在容器出現的次數
        letter_list.append((letter, str_seq.count(letter)))
    
    letter_list.sort(key=lambda x:x[1], reverse=True)'''
    
    
    #method2
    #使用Counter物件，為特殊形式的dict
    #使用 most_common() 將dict轉為list,如果呼叫時給予參數，表示指定回傳幾筆結果
    #format(*arg) => 記得要給*才能正確執行容器解包的行為
    letter_list = Counter(str_seq).most_common(1)
    
    return '{:2s}重複了{:1d} 次'.format(*letter_list[0])

    
print(most_repeated_letter('independence'))
    