#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:12:56 2023

@author: ml
"""
def run_timing():
    total_time = 0
    count = 0

    #使用指派運算式 變數:=值，簡化程式碼(空字串在判斷式視為False)
    while time := input('輸入跑10公里時間：(直接按Enter結束)'): 
        
        #檢查使用者是否輸入數值資料
        #isgigit()無法判別小數點是否能轉換為浮點數
        try: 
            total_time += float(time)
            count+=1
        except:
            print('請確認輸入資料是否為數值格式：'+time)
            
        
    if count > 0:
        print('跑 ', count, ' 次的平均時間為 ', total_time/count, ' 分鐘')        
    else:
        print('您未輸入任何資料')
        

run_timing()