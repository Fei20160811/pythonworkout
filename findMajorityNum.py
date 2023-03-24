#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:50:28 2023

@author: ml
"""
from collections import Counter

def find_majority_num(data):
    #method1 Counter()
    #Counter()統計各元素的數量
    #Counter().most_common() 回傳一個list 元素為(值，出現次數)
    #return Counter(data).most_common(1)[0][0]
    
    #method2 count()
    #使用set找出不重複元素 然後用count()產生類似Counter的統計表
    #return sorted([(data.count(num), num) for num in set(data)], reverse=True)[0][1]
    
    #method3 mode()
    import statistics
    return statistics.mode(data)

print(find_majority_num([5, 7, 6, 5]))
print(find_majority_num([1, 2, 2, 3, 2, 3, 1]))

