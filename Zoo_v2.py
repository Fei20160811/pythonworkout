#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:24:23 2023

@author: ml
"""
from dataclasses import dataclass
from typing import List


#用@dataclass 裝飾器簡化定義類別的手續
#@dataclass會自動實作__init__()和__repr__()
@dataclass
class Animal:
    color:str
    leg_num:int
    
    #@dataclass會將定義的屬性全部放入__init__()當成參數
    #__post_init__()會在__init__()後才執行，於此fun內可設定後續呼叫才給的參數
    def __post_init__(self):
        self.species = self.__class__.__name__
        
    def __repr__(self):
        return f'{self.color}色 {self.species} ({self.leg_num}條腿)'
        
#可以使用@dataclass(repr=False)来禁用自动生成的__repr__方法
#讓子類去找尋父類自定義的__repr__方法

#子物件同樣得加上@dataclass裝飾器
#於leg_num給預設值，讓子類別呼叫__init__()時可以跳過這個屬性
#class Elephant(Animal):
#    def __init__(self, color, leg_num=4):
#        super().__init__(color, leg_num)

@dataclass(repr=False)
class Elephant(Animal):
    leg_num : int =4
    
@dataclass(repr=False)
class Zebra(Animal):
    leg_num : int =4
    
@dataclass(repr=False)
class Snake(Animal):
    leg_num : int =0
    
@dataclass(repr=False)
class Parrot(Animal):
    leg_num : int =2
    
    
@dataclass
class Exhibit:
    area_num : int
    
    #比較寫在__post__init__內與外的差異
    def __post_init__(self):
        self.area_animals = []
    
    def add_animals(self, *animals):
        for animal in animals:
            self.area_animals.append(animal)
    
    def __repr__(self):
        return f'展示區編號{self.area_num}:' + f'{",".join ([str(item) for item in self.area_animals])}'
    
@dataclass
class Zoo:
    
    def __post_init__(self):
        self.exhibits_list = []
        
    def add_exhibits(self,*exhibits):
        for ex in exhibits:
            self.exhibits_list.append(ex)
            
    def animal_by_colr(self, color):
        return ','.join([str(animal) for ex in self.exhibits_list for animal in ex.area_animals if animal.color == color])
    
    def animal_by_leg_num(self, leg_num):
        return ','.join([str(animal) for ex in self.exhibits_list for animal in ex.area_animals if animal.leg_num == leg_num])
    
    def animal_total_leg_num(self):
        return sum([animal.leg_num for ex in self.exhibits_list for animal in ex.area_animals])

    def __repr__(self):
        #讓換行符號能正常於f-string運作
        nextline = '\n'
        return f'動物園：\n' + f'{nextline.join([str(item) for item in self.exhibits_list])}'        
    
elephant = Elephant('灰')
zebra = Zebra('黑白')
snake = Snake('綠')
parrot = Parrot('灰')

ex1 = Exhibit(1)
ex2 = Exhibit(2)
ex1.add_animals(elephant, zebra)
ex2.add_animals(snake, parrot)
zoo = Zoo()
zoo.add_exhibits(ex1, ex2)

print(elephant)
print(zebra)
print(snake)
print(parrot)
print('_______________________')
print(ex1)
print(ex2)
print('_______________________')
print(zoo)
print('_______________________')
print('灰色動物:[', zoo.animal_by_colr('灰'),']')
print('4條腿的動物:[', zoo.animal_by_leg_num(4), ']')
print('腿的總數:', zoo.animal_total_leg_num())