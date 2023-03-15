#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:47:36 2023

@author: ml
"""

import json
from collections import defaultdict

def print_scores(file_path):
    
    with open(file_path) as json_file:
        #將json文檔解析為dict
        json_dic = json.load(json_file)
        #記錄同科分數，預設為空list
        result_dic = defaultdict(list)
        
        print('班級： ', json_dic.get("class"))
        
        for record in json_dic.get("score"):
            for subject, score in record.items():
                #當第一次用某科的鍵名查詢defaultdict時，會建立此鍵，並用list()的回傳值當做此鍵的值
                #因有空list，所以可以呼叫append()
                #將同科的分數放在同一個清單內(該鍵對應的list)
                result_dic[subject].append(score)
        
        for subject, scores in result_dic.items():
            print('科目： ', subject)
            print('\t最高分： ', max(scores))
            print('\t最低分： ', min(scores))
            print('\t平均： ', sum(scores)/len(scores))
            
        
        
#print_scores(r'./sample/9a.json')