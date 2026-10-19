# operators 

'''Math - +,-,/,*,%
logical - and(&&) or(|) not(!)

and -- returns true if all cond true-- 

or -- any one cond true 

not(!) --- if cond true -- then false sesction will be executed,



relational - <,>,<=,>=!= ,==

assigment - +=,-=.*=,/=,=

increment/decrement - a++,++a

bitwise -- left shift,right shift,and,or

conditional/ternary  - ? :

decision Conditional Statements --

1. selection statement  -- if,elsif,else ladder

2. Looping statement -- for ,while

3. Branching statement --- switch case statement

'''
print("hi")

# selection statement  syntax -- 

'''
if condition:
    statement1
else:
    statement2

if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    default statement

'''

# print student grade calculator. accept 3 subject marks fom user and print grade

'''
per             grade 
>70              A+
60-70            A
50-60            B
40-50            C
< 40             D 

'''

m1,m2,m3= [int(x) for x in (input("enter marks")).split()] 

total = m1+m2+m3 

avg = int(total/3)

grade =""

if avg >=70:
    grade="A+"
elif avg>=60 and avg <=70:
    grade="A"
elif avg>=50 and avg<=60:
    grade="B"
elif avg>=40 and avg<=50:
    grade="C"
else:
   grade="Fail"

print(f"{m1} {m2} {m3} {total} {avg} {grade}")


# ATM Simulation 

# balance = 10000 

'''
ATM Menu 

1. check balance
2. Deposit amount 
3. Withdrwal amount
4. Exit 
'''












