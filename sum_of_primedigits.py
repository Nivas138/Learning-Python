# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:55:34 2018

@author: Nivas
"""

def prime(number):
    flag=1
    if number is 0 or number is 1:
        flag=0
    elif number == 2:
        flag=1
    elif number%2 == 0:
        flag=flag+1
    else:
        for j in range(3,number,2):
            if number%j == 0:
               flag=flag+1
               break
            else:
               continue
    return flag
print('Sum of prime digits in a given number')
num=int(input("Enter a number: "))
sum=0
flags=1
while num>0:
    numb=int(num)%10
    flags=prime(int(numb))
    if flags is 1:
        sum=sum+int(numb)
    num=int(num)/10
    if num is 0:
        break
print(sum)
