# number reverse -- 123 == 321
# pallindrome,count digits,reverse number,amstrong,

#num = int(input("Enter any number"))

# rev = 0 
# while num!=0:   
#     digit = num % 10   
#     rev = rev*10+digit  
#     num = num//10  

# print("Reverse Number :- ",rev)

num = 123
count_digit=0
temp = num
rev=0
for i in range(len(str(num))):
    digit =num %10
    rev = rev*10+digit 
    num = num//10

if temp == rev:
    print("Number is Pallindrome")
else:
    print("Not Pallindrome")

print("Reverse :-",rev)
print("Digits Count:-",len(str(temp)))

# Amstrong,Fibbonacci ,Prime

