#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:39:53 2023

@author: ml
"""
#可走訪物件與走訪器的分離
class MyEnumerate:
    
    #初始化寫入資料並記錄元素索引
    def __init__(self, data):
        self.data = data
        self.index = 0
        
    #傳回物件本身當作走訪器
    def __iter__(self):
        return self
    
    def __next__(self):
        #如果索引超過資料長度，引發StopIteration例外
        if self.index >= len(self.data):
            raise StopIteration
        #以tuple形式傳回(索引，值)
        value = (self.index, self.data[self.index])
        self.index += 1
        return value
    
myEnum = MyEnumerate('abcde')
for index, letter in myEnum:
    print(f'{index} -> {letter}')

#再次走訪會出錯
#print(myEnum.__next__())
