# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:24:01 2020

@author: Sushmita
"""

list1=[1,5,8]
list2=[4,7,10,12]
list3=list1+list2
print(list3)
sort_list = []
while list3:
    minimum = list3[0]
    for item in list3:
        if item < minimum:
            minimum = item
    sort_list.append(minimum)
    list3.remove(minimum)

print(sort_list)
