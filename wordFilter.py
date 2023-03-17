#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:05:15 2023

@author: ml
"""

def vowel_word(word):
    return len(set([character for character in word if character in 'aeiou']))


def word_filter(file_path):
    #method1
    '''
    #我的練習答案
    with open(file_path) as file:
        return [word for line in file for word in line.replace('.','').split() if vowel_word(word) > 2]'''
    
    #method2
    #用set建立母音表，與傳入單字做交集運算，算出相同個數   
    vowel = { 'a', 'e', 'i', 'o', 'u' }
    
    with open(file_path) as file:
        return [word for line in file for word in line.replace('.','').split() if (len(set(word) & vowel)) > 2]

print(word_filter(r'./sample/text2.txt'))