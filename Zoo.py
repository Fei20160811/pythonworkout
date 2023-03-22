#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:54:58 2023

@author: ml
"""
class Animal:
    
    def __init__(self, color, leg_num):
        #透過 ＿＿class__.__name__ 取得類別名稱
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num
        
    '''def __repr__(self):
        #!r若值是字串，印出時會加上單引號
        return f'{self.species}(color={self.color!r}, leg_name={self.leg_num!r})'''
    def __repr__(self):
        return f'{self.color}色 {self.species} ({self.leg_num}條腿)'
        

class Elephant(Animal):
    
    def __init__(self, color):
        #使用super()取得父類別，再呼叫其__init__()
        super().__init__(color, 4)
               
        
class Zebra(Animal):
    
    def __init__(self, color):
        super().__init__(color, 4)
         
class Snake(Animal):
    
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
        
    def __init__(this, color):
        super().__init__(color, 2)
        
class Exhibit:
    
    def __init__(self, area_num):
        self.area_num = area_num
        self.area_animals = []
        
    def add_animals(self,*animals):
        for animal in animals:
            self.area_animals.append(animal)
     
    def __repr__(self):
        return f'展示區編號{self.area_num}:' + f'{",".join([str(item) for item in self.area_animals])}'
    
class Zoo:
    
    def __init__(self):
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
        '''nextline = '\n'
        return '動物園：\n' + f'{nextline.join([str(item) for item in self.exhibits_list])}'''
        return '動物園：\n' + '\n'.join([str(item) for item in self.exhibits_list])

            
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