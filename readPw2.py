#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:55:01 2023

@author: ml
"""

def readPw2(path_file):
    
    with open(path_file) as file:
        #以生成式產生容器的方向
        #先讀出一個list，每個元素是每一行的字串，然後用split()將各行分割成子list，這樣每一行的單字不會跟其他行混在一起
        #有了此容器後，再用另一個生成式去走訪它
        return { words[0]:words[2] for words in [line.split(':') for line in file] }

print(readPw2(r'./sample/passwd.cfg'))