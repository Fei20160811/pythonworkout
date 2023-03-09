#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:42:04 2023

@author: ml
"""
def pl_sentence():
    input_sentence = input('請輸入一個英文句子：')
    #用list收集轉換過的單字
    translate_sentence = []
    
    for word in input_sentence.lower().split(' '):
        
        head_char = word[0]
        
        if head_char in 'aeiou':
            new_word = f'{word}way'
        else:
            new_word = f'{word[1:]}{head_char}ay'
            
        translate_sentence.append(new_word)
    
    #join() 將list的字串元素串成一個字串    
    print(' '.join(translate_sentence))
    
pl_sentence()