#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:39:21 2023

@author: ml
"""

import os
import readJson

import pathlib

import glob

def print_dir_scores(dir_path):
    
    #method1
    '''
    #os.listdir(dir_path) 列出資料夾內所有檔案名稱
    for file in os.listdir(dir_path):
        
        #string.endwith(str) 使用str過濾所需檔案副檔名
        if file.endswith('.json'):
            #使用自己所寫另個檔案的程式碼 import 檔案名稱  ＆檔案名稱.fun()
            #組合檔案完整路徑字串 os.path.join(dir_path, file)
            readJson.print_scores(os.path.join(dir_path, file))
            print('\n')
    '''
    
    #method2
    '''
    #pathlib
    #建立pathlib的 PosixPath物件
    p = pathlib.Path(dir_path)
    
    #走訪PosixPath物件會列出含路徑的檔名
    for file in p.iterdir():
        #判斷檔名結尾是否為 .json
        if file.suffix == '.json':
            readJson.print_scores(file)
            print('\n')'''
    
    #method3
    #glob
    #使用正規表達式 *.json過濾檔名
    for file in glob.glob(dir_path + '/*.json'):
        readJson.print_scores(file)
        print('\n')
        

print_dir_scores(r'./sample')