#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:03:33 2023

@author: ml
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, num):
        self.data.append(num)
        
    def pop(self):
        if self.data:
            #我的答案
            '''
            value = self.data[-1]
            self.data = self.data[:-1]
            return value'''
            return self.data.pop()
        else:
            return '堆疊已無資料'
            
    def top(self):
        if self.data:
            return self.data[-1]
        else:
            return '堆疊無資料'
            
    def min_num(self):
        if self.data:
            return min(self.data)
        else:
            return '堆疊無資料'
            
    def max_num(self):
        if self.data:
            return max(self.data)
        else:
            return '堆疊無資料'
            
            
stack = Stack()
stack.push(3)
stack.push(2)
stack.push(8)
stack.push(6)
stack.push(5)

print(stack.pop())
print(stack.top())
print(stack.min_num())
print(stack.max_num())