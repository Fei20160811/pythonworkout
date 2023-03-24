#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:39:13 2023

@author: ml
"""
def reverse_num_digits(data):
    #將數字轉成字串，反轉後再轉回數字
    #切片 list[起始索引：結束索引(不含)：步長] 設為-1會倒著取值
    #先用abs取絕對值，轉回新數字後再根據原本的正負做相對應的處理
    answer = int(str(abs(data))[::-1]) * (1 if data > 1 else -1)
    return answer

print(reverse_num_digits(123))
print(reverse_num_digits(-456))
print(reverse_num_digits(-240))