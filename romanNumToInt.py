#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 17:04:07 2023

@author: ml
"""
def roman_num_to_int(data):
    #method1 使用迴圈
    '''
    roman_dict = { "I":1,
                   "V":5,
                   "X":10,
                   "L":50,
                   "C":100,
                   "D":500,
                   "M":10000
                 }
    
    total_value = 0
    pre_value = 0
    
    for char in data:
        now_value = roman_dict.get(char)
        total_value += now_value
        if pre_value < now_value:
            total_value -= 2* pre_value
        pre_value = now_value
        
    return total_value'''

    #使用lsit生成式
    roman_dict = { "I":1,
                   "V":5,
                   "X":10,
                   "L":50,
                   "C":100,
                   "D":500,
                   "M":10000
                 }
    roman_special = { "IV":-2,
                      "IX":-2,
                      "XL":-20,
                      "XC":-20,
                      "CD":-200,
                      "CM":-200
                    }
    #由使用者給的字串逐一至dict取值後相加
    standard_result = sum([roman_dict.get(c) for c in data])
    #拿roman_special dict中的所有字串比對使用者傳入字串是否有相符者，有則從dict取值相加
    special_result = sum([value for index, value in roman_special.items() if index in data])
    return standard_result + special_result

print(roman_num_to_int('II'))
print(roman_num_to_int('IV'))
print(roman_num_to_int('MMCDXIX'))
    