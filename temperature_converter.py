while True:
    print("\t\tMENU")
    print("\t1.Celsius to Fahrenheit")
    print("\t2.Fahrenheit to Celsius")
    print("\t3.Exit")
    choice = int(input("Enter choice: "))
    if choice==1:
        celsius_degree = int(input("Enter the degree in celsius: "))
        fahrenheit_degree = (celsius_degree * 9/5) + 32
        print(f"The Fahrenheit degree for Celsius degree {celsius_degree} is {fahrenheit_degree}")
    elif choice==2:
        fahrenheit_degree = int(input("Enter the degree in fahrenheit: "))
        celsius_degree = (fahrenheit_degree - 32) * 5/9
        print(f"The Celsius degree for Fahrenheit degree {fahrenheit_degree} is {celsius_degree}")
    elif choice==3:
        print("Exiting Temperature Converter")
        break
    else:
        print("Invalid Choice")