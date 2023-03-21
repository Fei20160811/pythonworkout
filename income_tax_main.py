#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:35:42 2023

@author: ml
"""

#套件匯入方式
#method1
from tax import income_tax
#method2
import tax.income_tax

#模組匯入方式
#from income_tax import calculate_tax
#print(calculate_tax(77000)) 

print(income_tax.calculate_tax(77000)) 
print(tax.income_tax.calculate_tax(77000)) 
    