# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 16:08:36 2018

@author: Nivas
"""
A = list()
count=0
sum=0
print("Array Operations-Sum of Counts of key Divisibles")
print("Enter a number of array elements")
n=int(input())
for i in range(0,n):
    print("Element",i+1)
    num=input()
    A.append(int(num))
    count+=1
print("Array:",A)
print("Enter a Key: ")
key=int(input())
for j in range(0,count):
    if A[j]%key == 0:
        div_number=int(A[j]/key)
        sum+=div_number
    else:
        div_number=int(A[j]/key)
        sum=sum+div_number+1
print(sum)