#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:55:29 2023

@author: ml
"""
import time, random

def elapsed_time_gen():
    last_time = time.perf_counter()
    while True:
        now = time.perf_counter()
        #傳回經過的時間長
        yield now - last_time
        #更新last_time 最後取值的時間
        last_time = now
    

elapsed_time = elapsed_time_gen()
for _ in range(10):
    time.sleep(random.randint(1, 10) / 10)
    print(next(elapsed_time))