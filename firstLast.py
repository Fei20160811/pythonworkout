#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:22:27 2023

@author: ml
"""
def first_last(seq_obj):
    #在list or tuple 中如果單用索引取元素，實際上相加的是元素本身
    #必須用切片的方式取元素。此時元素是單一元素的同型別容器
    return seq_obj[:1] + seq_obj[-1:]


print(first_last('abcde'))
print(first_last([1,2,3,4,5]))