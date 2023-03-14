#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:32:56 2023

@author: ml
"""

def wordcount(file_path):
    
    text_dict = {}
    
    Characters = 0
    Words = 0
    word_set = set()
    Lines = 0
    
    with open(file_path) as file:
        
        for line in file:
            
            #計算每行字元素
            Characters += len(line)
            
            #將每行的單字拆出 
            #spiit() v.s. split(' ')
            for word in line.split():
                #為計算不重複單字數而準備
                word_set.update(word)
                #計算全部單字數，不論有無重複
                Words += 1
                
            Lines += 1
            
    text_dict.update({'Characters':Characters})
    text_dict.update({'Words':Words})  
    text_dict.update({'Unique Words':len(word_set)})    
    text_dict.update({'Lines':Lines})  

    for key, value in text_dict.items():
        print(f'{key}: {value}')
      

wordcount(r'./sample/text.txt')