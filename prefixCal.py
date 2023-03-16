#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:14:26 2023

@author: ml
"""

import operator

#只有method1 operation需要用到下列區塊的函式定義
'''
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b'''

#檢查是否為整數或浮點數函式
#isdigit() v.s. isnumeric() ???
def isNumber(num):
    return num.replace('.', '').isdigit()


def prefix_cal(to_solve):
    
    #用dict來收集各個計算函式
    #method1
    '''
    operation = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div 
        }'''
    
    #method2
    '''
    #用lambda簡化函式定義
    operation = {
        '+': lambda a, b: a+b,
        '-': lambda a, b: a-b,
        '*': lambda a, b: a*b,
        '/': lambda a, b: a/b
        }'''
    
    #method3
    #用operator模組
    operation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
        }
    
    prefix_list = to_solve.split(' ')
    prefix_len = len(prefix_list)
    
    #每次進入迴圈重算一次list大小
    while len(prefix_list) > 1:
        for i in range(prefix_len - 2):
            #每三個一組切片
            cal, num1, num2 = prefix_list[i:i+3]
            #檢查是否符合計算字符，皆兩個數字的型態，如符合型態則終止迴圈
            if cal in operation and isNumber(num1) and isNumber(num2):
                break;
        #計算符合形態的組合資料
        result = operation.get(cal)(float(num1), float(num2))
        #將結果組合回prefix_list做後續運算
        #結果要記得轉回str
        prefix_list =  prefix_list[:i] + [str(result)] +  prefix_list[i+3:]
    
    return prefix_list[0]

print(prefix_cal('/ * + 2 4 3 + 1 5'))