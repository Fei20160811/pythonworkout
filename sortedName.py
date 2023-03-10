#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:03:23 2023

@author: ml
"""

import operator

def alphabetize_names(obj):
   result = [] 
    
   #method1:
   #lambda匿名函式 函式＝lambda 參數：運算式
   #使用tuple完成先排序姓 後排序明的需求
   #name_list = sorted(obj, key=lambda x:(x[1],x[0]))
   
   
   #method2:
   #operator.itemgetter() 當容器內的元素也是容器時可使用
   name_list = sorted(obj, key=operator.itemgetter(1, 0))

   for item in name_list:
       result.append(f'{item[1]}, {item[0]}, {item[2]}')
       
   return '\n'.join(result)

          
people = [
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'primeminister@canada.gov'),
    ('Angela', 'Merkel', 'primeminister@germany.gov'),
    ('Jacinda', 'Ardern', 'primeminister@newzealand.gov')]    
    
print(alphabetize_names(people))