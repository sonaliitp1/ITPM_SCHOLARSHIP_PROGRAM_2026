# To check given number is prime or not 
import math

n = 10//2

print(n)

num = int(input("Enter number "))
flag=0

if num <=1:
    print("Given number is not prime")
else:

    for i in range(2,math.sqrt(num)+2):  
        if num%i==0:
            flag=1

if flag==0:
    print("Number is prime")
else:
    print("Number is not prime")



           



