#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:32:03 2023

@author: ml
"""
def sorted_grades(obj):
    result = []
    #reverse => 預設由小到大，需調整
    grades_list = sorted(obj, key=lambda g:g[2], reverse=True)
    
    #method1:
    #f-string
    '''for first, last, grade in grades_list:
        #加入字串格式 12s/10s => 表佔12格 or 10格 .1f => 表不指定整數位數，小數點四捨五入到1位
        result.append(f'{last:12s} {first:10s} {grade:.1f}')'''
        
     #method2:
     #format() & 容器解包
    for item in grades_list:
        result.append('{:12s}{:10s}{:.1f}'.format(*item))

    return '\n'.join(result)


grades = [
    ('Alice', 'Wooding', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
    ]

print(sorted_grades(grades))