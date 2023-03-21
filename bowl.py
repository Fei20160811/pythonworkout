#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:21:52 2023

@author: ml
"""
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        
    def __repr__(self):
        return f'Scoop({self.flavor})'
        
class Scoop_Maker:
    #記得method也要加self 
    def create(self, flavors):      
        return [Scoop(flavor) for flavor in flavors]
            
'''scoop_maker = Scoop_Maker()
scoops = scoop_maker.create(['巧克力', '香草', '薄荷'])
for scoop in scoops:
    print(scoop.flavor)'''
    
    
class Bowl:
    max_scoops = 3 #類別屬性 => 不管從物件或類別查詢該屬性，皆能找到
    
    
    def __init__(self):
        self.scoops = []
        #self.max_scoops = 3 物件屬性 ＝>所有實例物件個別新增一個容量限制的屬性
    
    def add_scoop(self, *scoop_item):
        for item in scoop_item:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(item)
    
    def show_content(self):
        return '/'.join([scoop.flavor for scoop in self.scoops])
    
    #__str__ 傳回代表物件的非正式字串，給一般使用者參考
    #__repr__ 傳回代表物件的正式字串，給程式設計師除錯用
    #當使用者用str() print()或字串格式化功能印出物件時，就會呼叫此兩種方式
    #若找不到__str__ 就會改而呼叫 __repr__
    '''def __str__(self):
        flavors = '/'.join([scoop.flavor for scoop in self.scoops])
        return f'冰淇淋碗口味：{flavors}'''
    
    def __repr__(self):
        return f'Bowl(scoop={self.scoops})'
    
bowl = Bowl()
bowl.add_scoop(Scoop('薄荷巧克力'))
bowl.add_scoop(Scoop('開心果'), Scoop('百香果'))
bowl.add_scoop(Scoop('抹茶'), Scoop('芒果'))

#print(bowl.show_content())
print(bowl)
print('________________________________________')
    
#物件繼承
class ExtraBowl(Bowl):
    max_scoops = 5
    
bowl = ExtraBowl()
bowl.add_scoop(Scoop('薄荷巧克力'))
bowl.add_scoop(Scoop('開心果'), Scoop('百香果'))
bowl.add_scoop(Scoop('抹茶'), Scoop('芒果'))

print(bowl)
    

            

