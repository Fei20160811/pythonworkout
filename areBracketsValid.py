#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:34:57 2023

@author: ml
"""
def are_brackets_valid(data):
    
    #括號對照表
    symbol_dict = {
         "(": ")",
         "{":"}",
         "[":"]"
        }
    
    #記錄括號的堆疊
    symbol_stack = []
    
    for char in data:
        if char in symbol_dict:
            #若char為左括號，將對應的右括號放入stack
            symbol_stack.append(symbol_dict.get(char))            
        else:
            #若堆疊不為空且取出的值和右括號不符，表格式無效
            #若symbol_stack為空，在判斷式代表為False，則程式不會再去檢查右邊的條件式
            if not(symbol_stack and symbol_stack.pop() == char):
                return False
    #若走訪完堆疊空了代表格式有效，反之則否
    return True if not symbol_stack else False

    
print(are_brackets_valid('[]'))
print(are_brackets_valid('[()]'))
print(are_brackets_valid('[()]{}'))

print(are_brackets_valid('([)]'))
print(are_brackets_valid('[]('))
print(are_brackets_valid(')'))