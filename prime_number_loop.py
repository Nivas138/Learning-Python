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
print('Prime Number within Limit')
num=int(input("Enter a limit: "))
for i in range(0,num):
    flag=1
    flags=prime(i)
    if flags is 1:
        print (i)
