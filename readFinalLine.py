#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:21:39 2023

@author: ml
"""
def read_final_line(file_path):
    #r'' => 將字串轉為raw字串，避免特殊字元的解讀錯誤
    #open() 預設為讀取模式
    #讀取檔案的錯誤處理 with => 專門用來搭配資源管理器，建立和結束資源管理器物件時，會自動呼叫相關的method取得或釋放資源，並能攔截潛在錯誤
    #open傳回的檔案物件是資源管理器，搭配使用with，結束後會自動呼叫close()關閉資料流
    with open(file_path, 'r') as f:
         
        #method1
        '''
        #readline() 一次只讀一行，讀到檔案結尾回傳空字串
        while line := f.readline():
            lastline =line
        
        return lastline'''
    
        #method2
        #open() 傳回的檔案物件支援走訪器協定
        #檔案物件不是容器無法用f[-1]的方式取值
        #for迴圈的line變數於迴圈結束後不會消失
        for line in f:
            pass
        
        return line
    

print(read_final_line(r'./sample/login.log'))