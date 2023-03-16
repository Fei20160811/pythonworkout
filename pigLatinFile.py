#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:19:47 2023

@author: ml
"""

import pigLatin

def pl_file(file_path):
    
    with open(file_path) as file:
        return  ' '.join(pigLatin.pig_latin(word.lower().replace('.','')) 
                         for line in file for word in line.split())

print(pl_file(r'./sample/text2.txt'))
    
