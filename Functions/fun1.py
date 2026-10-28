

def fun(**kwargs):

    print(kwargs)

    for key,value in kwargs.items():
        print(f"{key} :- {value}")

fun(name="john",age=23)


'''

*args -  accpets multiple positional arguments 

**kwgrgs -- accept multiple keyword arguments

default arguments

'''
print("___________________________")

def fun1(a,b,c=10):
    print(a+b+c)

fun1(20,30,40)

print("__________________________")

# NADK -- normal arguments,args argument,default argument,kwargs argument

def test(c,d,*args,t=100,**kwargs): # * args with normal argument
    m =1
    for i in args:
        m*=i
    print(m)
    print(c,d,t)
    print(kwargs)

test(10,20,4,3,5,name="john",age=23)


# Lambda Function -- It is small anonymous python function

# lambda arguments : expression


import math



def square(n):
    return n*n

square(5)

sq = lambda n,p : n*p

print(sq(5,3))

is_even = lambda n:n%2==0

print(is_even(20))


# print greatest number - 20 30 

max_number = lambda n,p: n if n>p else p

print("Max Number :- ",max_number(20,45))


# map ,filter 

numbers =[25,64,16,55,81]


# map(function,iterables)  fun- user defined function,lambda,inbuilt function

# square each element in numbers list

result =list(map(lambda x :x*x,numbers))

result1 = list(map(square,numbers))

result2 = list(map(math.sqrt,numbers))

print(result)

print(result1)

print(result2.round(2))








