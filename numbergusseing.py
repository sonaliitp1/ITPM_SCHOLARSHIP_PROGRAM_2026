'''
guess_number  - 121

attempts = 5

enter number -- 150  --- too high   too low 


'''

guess_number=121

attempts = 5 

while attempts >0 :
    guess = int(input("enter number"))

    if guess == guess_number:
        print("Congratulation .... Correct Guess")
    elif guess > guess_number:
        print("Too high")
    elif guess < guess_number:
        print("Too low")
    attempts-=1
    print("Attempts pending:-",attempts)

if attempts==0:
    print("Game over and Guess Number is :-",guess_number)

# make half faluty calculator 
'''
Accept 2 nos and one perator from user and print correct result except following

 expression

23 + 49 = 555

56 / 9 = 90 

34 * 7 = 123

23 + 3 = 26

'''





