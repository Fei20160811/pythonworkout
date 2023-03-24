#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:25:44 2023

@author: ml
"""
#繼承list型別
class Stack_v2(list):
    #self就是list本身
    #top()因為list本身已經有了，再重新定義會讓Stack的pop()不斷呼叫自己產生遞迴錯誤
    def push(self, x):
        self.append(x)
        
    def top(self):
        if self:
            return self[-1]
        else:
            return '堆疊無資料'
    
    def min_num(self):
        if self:
            return min(self)
        else:
            return '堆疊無資料'
    
    def max_num(self):
        if self:
           return max(self)
        else:
            return '堆疊無資料'    
    
        
stack = Stack_v2()
stack.push(3)
stack.push(2)
stack.push(8)
stack.push(6)
stack.push(5)

print(stack.pop())
print(stack.top())
print(stack.min_num())
print(stack.max_num())