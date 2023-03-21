#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:04:47 2023

@author: ml
"""

def menu(**funs):
    
    #定義閉包函式(menu物件)
    def menuFun():
        #將關鍵字內容串起來，當成給使用者的輸入提示
        option_str = '/'.join([key for key in funs.keys()])
        
        
        while True:
            choice = input(f'選擇項目({option_str})')
            if choice in funs:
                #傳回使用者要求的函式
                return funs.get(choice)
                break
            print('選項不存在')
                
    return menuFun
            


#加入測試程式碼
#檔案執行時會擁有__name__變數，若該檔案是由使用者直接執行，變數內容就是'__main__',利用此特性試驗該檔案功能
#若檔案被當成模組匯入，__name__變數內容會是模組名稱
if __name__ == '__main__':
    import operator
    
    a, b = 10, 3
    my_menu= menu(add = operator.add,
                  sun = operator.sub,
                  mul = operator.mul,
                  div = operator.truediv)
    print(my_menu()(a,b))