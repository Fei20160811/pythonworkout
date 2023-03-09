#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:52:39 2023

@author: ml
"""
import random

def guessing_game():
    #回傳一個隨機整數 N，使得 a <= N <= b
    answer = random.randint(0, 99)
    print('數字答案：', answer, '\n\n')
    
    try:
        while True:
            #使用input()輸入資料
            input_str = input('請猜數字(0~99):')
            
            #isdigit()檢查輸入值是否為整數
            if input_str.isdigit():
                #int()將字串資料轉成數值
                user_guess = int(input_str)
            
                if user_guess > answer:
                    user_guess = print('猜的太高，請再試一次\n')
                elif user_guess < answer:
                    user_guess = print('猜的太低，請再試一次\n')
                else:
                    print('答對了！答案是 ', answer)
                    break  
            else:
                print('請輸入整數數值\n')
    except:
        print('異常錯誤，請通知開發人員')
    

guessing_game()