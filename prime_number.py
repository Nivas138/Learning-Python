# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 12:46:59 2018

@author: Nivas
"""
def prime(number):
    #number = int(input("Enter a number: "))
    if number is 0 or number is 1:
        print("Not Prime")
    elif number == 2:
        print("Prime Number")
    elif number%2 == 0:
        print("Not prime")
    else:
        flag=1
        for i in range(3,number,2):
            if number%i == 0:
               flag=flag+1
               break
            else:
               continue
        if flag is 1:
            print ("Prime")
        else:
            print("Not Prime")
print('Prime Number')
num=int(input("Enter a number: "))
prime(num)
while True:
    print("Do you want to continue:y/n")
    choose=str(input())
    if choose is 'y' or choose is 'Y':
        numb=int(input("Enter a number: "))
        prime(numb)
    else:
        break