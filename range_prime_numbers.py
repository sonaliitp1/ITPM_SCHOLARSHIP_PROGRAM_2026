# To check given number is prime or not 
import math

fn = int(input("Enter first number"))
ln = int(input("Enter last number")) 

if fn < ln :  
    for i in range(fn,ln+1):  
        flag=0
        for j in range(2,int(math.sqrt(i))+2): 
            if i%j ==0:  
                flag=1
                break
        if flag == 0:
            print(i,end=" ")

else:
     for i in range(ln,fn+1):
            flag=0
            for j in range(2,int(math.sqrt(i))+2):
                if i%j ==0: 
                    flag=1
                    break
            if flag == 0:
                print(i,end=" ")

'''
1. Fibbonacci Series 
2. Amstrong Number
3. Pallindrome
4. prime number
5. GCD 
6. Factorial 
7. Perfect Number
8. pattern programs

'''
    
