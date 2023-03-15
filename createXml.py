#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:48:12 2023

@author: ml
"""
#*args => 接收數量不定的關鍵字參數，只能接收到參數的值
#**kwargs => 接收數量不定的關鍵字參數，用dict物件接收參數的名稱&值
#數量不定的參數放最後面
def myxml(tag_name, content='', **attrs):
    
    attrs_list = []
    
    for key, value in attrs.items():
        attrs_list.append(f'{key}="{value}"')
        
    attrs_str = (' ').join(attrs_list)
    
    return f'<{tag_name} {attrs_str}>{content}<{tag_name}>'

print(myxml('foo', 'bar', a=1, b=2, c=3))