#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:25:48 2023

@author: ml
"""
import csv

def password_to_csv(orginal_f, new_f):
    
    #練習讀寫
    '''
    data = []
    
    with open(orginal_f) as file:
        #delimiter 指定分隔符號
        csv_reader = csv.reader(file, delimiter=':')
        
        for line in csv_reader:
            data.append([line[0], line[2]])
    
    #open('write_path', 'w') 建立並開啟要寫入的檔案
    with open(new_f, 'w') as file:
        
        csv_writer = csv.writer(file, delimiter='\t')
        
        #writerow 一次寫一行 
        #writerows 一次寫多行
        csv_writer.writerows(data)'''
    
    #開啟讀取檔案 & 寫入檔案
    #newline => None:使用系統預設換行符號 ‘’＝>沿用原檔案的換行符號
    with open(orginal_f) as read_f, open(new_f, 'w', newline='') as write_f:
            
        csv_reader = csv.reader(read_f, delimiter=':')
        #lineterminator='\n' 寫入時於每行結尾加上\n
        csv_writer = csv.writer(write_f, delimiter='\t', lineterminator='\n')
        
        for line in csv_reader:
            csv_writer.writerow([line[0], line[2]])
            
password_to_csv(r'./sample/passwd.cfg', r'./sample/userinfo.csv')