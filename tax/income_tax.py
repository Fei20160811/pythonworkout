#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:08:02 2023

@author: ml
"""

from decimal import Decimal

#定義自訂例外類別(繼承ValueError)
class IncomeIsNotNumberError(ValueError):
    pass

#float型別的小數點是用二進位儲存，多少有誤差，改用decimal精確性較高
tax_rate_dict = {
    0: Decimal(0.1),
    10001: Decimal(0.2),
    50001: Decimal(0.3),
    100001: Decimal(0.4),
    500001: Decimal(0.5)
    }


def find_tax_range(income):
    return [tax_rate_dict.get(key) for key in tax_rate_dict.keys() if key < income][-1]

#print(find_tax_range(77000))


def calculate_tax(income):
    
    #錯誤檢查
    if not (isinstance(income, int) or isinstance(income, float)):
        #raise ValueError('請輸入數值資料')
        raise IncomeIsNotNumberError('請輸入數值資料')
    
    #回傳時讚再轉回float
    return float(Decimal(income) * find_tax_range(income))
                 
#print(calculate_tax(77000))
    
