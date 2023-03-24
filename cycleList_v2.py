#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:53:15 2023

@author: ml
"""

from dataclasses import dataclass

@dataclass
class CycleIterator():
    data: list
    loop_num: int
    
    #index屬性不需要透過__init__()初始化，故用__post_init__()建立
    def __post_init__(self):
        self.index = 0
    
    def __next__(self):
        if self.index >= self.loop_num:
            raise StopIteration
            
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value
    

@dataclass
class CycleList:
    data:list
    loop_num:int
    
    def __iter__(self):
        return CycleIterator(self.data, self.loop_num)
    
    
clist = CycleList(['a', 'b', 'c'], 5)
for c in clist:
    print(c)
    
#再次走訪不會發生問題，傳回新的走訪器
print(clist.__iter__().__next__())