# To print multiplication table of given number 

# 5 * 1 = 5
'''
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
'''

num = int(input("enter number"))

for i in range(1,11):
    mul = num * i 
    print(f"{num} * {i} = {mul}")

# print multiplication tables on given range 
# 2 to 8 

'''
2 * 1 = 2  2 * 2 =4  ......
'''

fn = 2
ln = 8 

for i in range(fn,ln+1):
    for j in range(1,11):
        mul = i * j
        print(f"{i} * {j} = {mul}",end=" ")
    print()





