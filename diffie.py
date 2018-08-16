def prime(number):
    #number = int(input("Enter a number: "))
    if number is 0 or number is 1:
        return 0
    elif number == 2:
        return 1
    elif number%2 == 0:
        return 0
    else:
        flag=1
        for i in range(3,number,2):
            if number%i == 0:
               flag=flag+1
               break
            else:
               continue
        if flag is 1:
            return 1
        else:
            return 0
print("Enter the public variables P(prime) and G:generation point ")
p=int(input())
g=int(input())
print("Enter a Secret value a and b: ")
a=int(input())
b=int(input())
if prime(p)==1:
	print("KEY GENERATION = before EXCHANGE")
	x=pow(g,a) % p
	print("Key for a: ",x)
	y=pow(g,b) % p
	print("key for b: ",y)
	print("Exchanging key.....")
	a_rec=y
	b_rec=x
	print("KEY GENERATION = after EXCHANGE")
	sa=pow(a_rec,a) % p
	print("key for a: ",sa)
	sb=pow(b_rec,b) % p
	print("key for b: ",sb)
	print("checking Equal")
	if sa == sb:
		print("EQUAL = MESSAGE TRANSFERED")
	else:
		print("ERROR") 
else:
	print("ERROR")
