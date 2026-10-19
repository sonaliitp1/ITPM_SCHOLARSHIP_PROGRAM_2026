balance = 10000 

while True:
    print("******* ATM Simulation App *******")
    print()
    print("\t1. Check balance")
    print("\t2. Deposit amount")
    print("\t3. Withdrwal amount")
    print("\t4. Exit")

    choice = int(input("Enter your choice....."))

    if choice==1:
        print("Current Balance :- ",balance)
    elif choice==2:
        amount = float(input("Enter deposit amount"))
        balance+=amount
        print("Amount Deposit Successfully...")
    elif choice==3:
        amount = float(input("Enter withdrwal amount"))
        if amount <=0:
            print("Amount must be positive")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance-=amount 
            print("Withdrwal Successfully")
    else:
        print("Thank you for using atm ....")
        break
        

