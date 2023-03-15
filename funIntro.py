#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:21:19 2023

@author: ml
"""

#當呼叫函式時，python會比對 hello.__code__.co_argcount 的數量，如果不一致就會發生錯誤
#如希望參數是選擇性的，解決方式是給予一個預設值
#沒有預設值的參數(位置型參數)得寫在有預設值的參數前面(關鍵字參數)前面，否則會產生錯誤
def hello(name, greeting='Hello'):
    return f'{greeting}, {name}'

print(hello('world'))
#print(hello()) 

#使用指名方式傳值給參數時，順序可任意排列
print(hello(greeting='Hi there', name='python'))

#參數的數量
print(hello.__code__.co_argcount)
#參數的名稱
print(hello.__code__.co_varnames)

print('_________________________')
#LEGB L=>local
#     E=>enclosing function(子函式外父函式的變數，參數)
#     G=>global
#     B=>builtins(python內建函式，例外類別)
#sum 全域變數與python關鍵字名稱相同，覆蓋python關鍵字功能
sum = 0
for i in range(5):
    sum+=i
    
print(sum)
#python不會向上尋找內建函式sum()，所以發生錯誤
#print(sum([10, 20, 30]))

print('_________________________')
#x全域變數
x = 100

def foo():
    #在區域範圍修改全域變數(失敗)
    #當python在區域範圍找到x值後便不會再往上找
    #加上global關鍵字好，便可修改到全域變數值，避免此種做法
    #global x
    x = 200
    print(x)
    
print(x)
foo()
print(x)

print('_________________________')
#x全域變數
x = 0

#父函式
def foo(x, y):
    #子函式
    def bar():
        #仍使用父函式自己的變數
        #需加入nonlocal關鍵字，讓python尋找函式外層範圍指定的變數，跳過global層級
        #nonlocal x
        #嘗試修改父函式的變數x
        x = 20
    
    #呼叫子函式
    bar()
    return x * y

print(foo(10,10))


