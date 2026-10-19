sum=0 
# for i in range(1,50):
#     print(i,end=" ")
#     sum=sum+i
# print("\n Sum :-",sum)


for i in range(1,20,2):
    print(i)

# ask the user to enter first number and last number and print all numbers between # first and last

fn = int(input("Enter first number"))
ln = int(input("Enter second number"))
if fn <=ln:
    for i in range(fn,ln+1):
        print(i,end=" ") 
else:
    for i in range(fn,ln-1,-1):
        print(i,end=" ") 


