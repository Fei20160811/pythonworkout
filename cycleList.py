#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:56:59 2023

@author: ml
"""
#走訪器物件類別
class CycleIterator:
    
    def __init__(self, data, loop_num):
        self.data = data
        self.loop_num = loop_num
        self.index = 0
        
    def __next__(self):
        
        if self.index >= self.loop_num:
            raise StopIteration
            
        #使用％運算符號取餘數，這樣超過資料容器長度就會重頭算起
        value = self.data[self.index % len(self.data)]
        self.index +=1 
        
        return value
        
#可走訪物件類別
class CycleList:
    
    def __init__(self, data, loop_num):
        self.data = data
        self.loop_num = loop_num
        
    
    def __iter__(self):
        #傳回新的走訪器
        return CycleIterator(self.data, self.loop_num)
    
clist = CycleList(['a', 'b', 'c'], 5)
for c in clist:
    print(c)
    
#再次走訪不會發生問題，傳回新的走訪器
print(clist.__iter__().__next__())
    

        