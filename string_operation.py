# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:38:26 2018

@author: Nivas
"""

print("String Operations")
new_str=str(input("Enter a String: "))
len_str=len(new_str)
for i in range(0,len_str):
    for j in range(0,len_str):
        if i == j :
            print(new_str[i],end =" ")
        elif ((len_str-1)-i)==j:
            print(new_str[j],end =" ")
        else:
            print(" ",end =" ")
