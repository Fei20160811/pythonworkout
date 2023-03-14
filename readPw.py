#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:00:15 2023

@author: ml
"""

import pprint

def passwd_to_dict(file_path):
    
    user_dict ={}
    
    with open(file_path) as file:
        for line in file:
            user_info = line.split(':')  
            #readable
            user_dict.update({user_info[0]:user_info[2]})
            #user_dict[user_info[0]] = user_info[2]
    
    return user_dict

#pprin更美觀的輸出dict
#sort_dicts 印出時是否將內容依鍵排序輸出
pprint.pprint(passwd_to_dict(r'./sample/passwd.cfg'), sort_dicts=False)