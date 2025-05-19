balance = 1000

print("\t\tMENU")
print("\t1.Check Balance")
print("\t2.Deposit Amount")
print("\t3.Withdraw Amount")
print("\t4.Exit")
choice = int(input("Enter your choice:- "))   

while choice!=4:
    if choice == 1:
        print(f"Your Current Balance is: {balance}")
    elif choice == 2:
        deposit_amount = int(input("Enter the amount to be deposited: "))
        balance = balance + deposit_amount
        print(f"Your balance after depositing {deposit_amount} is {balance}")
    elif choice == 3:
        withdraw_amount = int(input("Enter the amount to be withdraw: "))
        if balance <= 1000:
            print("Can't withdraw money. Minimum balance should be 1000")
        else:
            balance = balance - withdraw_amount
            print(f"Money withdraw rupees {withdraw_amount }")
    elif choice == 4:
        exit()
    else:
        print("Invalid option")

    print("\t\tMENU")
    print("\t1.Check Balance")
    print("\t2.Deposit Amount")
    print("\t3.Withdraw Amount")
    print("\t4.Exit")
    choice = int(input("Enter your choice:- "))