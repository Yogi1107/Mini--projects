tasks = []

print("\t\tMENU")
print("\t1.Add")
print("\t2.Remove")
print("\t3.View")
print("\t4.Exit")
choice = int(input("Enter your choice:- "))
while choice!=4:
    if choice==1:
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added")
    elif choice == 2:
        task = input("Enter your task: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed")
        else:
            print("Task does not exists.")
    elif choice == 3:
        for i in tasks:
            print(i)
    elif choice == 4:
        exit()
    else:
        print("Invalid Choice")
    
    print("\t\tMENU")
    print("\t1.Add")
    print("\t2.Remove")
    print("\t3.View")
    print("\t4.Exit")
    choice = int(input("Enter your choice:- "))

