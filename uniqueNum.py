#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:05:34 2023

@author: ml
"""
def unique_num_len(numbers):
   return len(set(numbers))
  

numbers = [1, 2, 3, 1, 2, 3, 4, 1, 2]      
print(unique_num_len(numbers))