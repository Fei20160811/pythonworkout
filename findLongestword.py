#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:08:22 2023

@author: ml
"""
def find_longest_word(file_path):
    
    longest_word = ''
    word_set = set()
    
    with open(file_path) as file:
        
        for line in file:
            #method1
            #replace('.','')去掉單字結尾的.
            '''for word in line.replace('.','').split():
                if len(word) > len(longest_word):
                    longest_word = word'''
                    
            #method2
            #使用set
            word_set.update(line.replace('.','').split())
            #指定用單字長度排序，排序後取最後一個單字
            longest_word = sorted(word_set, key=len)[-1]
    
    return longest_word

print(find_longest_word(r'./sample/text2.txt'))
    