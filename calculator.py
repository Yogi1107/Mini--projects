while True:
    print("\t\tMENU")
    print("\t1.Addition")
    print("\t2.Subtraction")
    print("\t3.Multiplication")
    print("\t4.Division")
    print("\t5.Modulus")
    print("\t6.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"Addition of numbers {a} and {b} is {a+b}")
    elif choice == 2:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"Subtraction of numbers {a} and {b} is {a-b}")
    elif choice == 3:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"Multiplication of numbers {a} and {b} is {a*b}")
    elif choice == 4:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        if b<=0:
            print("Cannot divide by 0")
        else:
            print(f"Division of numbers {a} and {b} is {a/b}")
    elif choice == 5:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f"Modulus of numbers {a} and {b} is {a%b}")
    elif choice == 6:
        print("Exiting Simple calculator")
        break
    else:
        print("Invalid Choice")