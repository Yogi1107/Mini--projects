items = []
quantities = []

while True:
    print("\n===== Inventory Menu =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Remove Item")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item name: ").lower()
        quantity = int(input("Enter quantity: "))
        
        if item in items:
            index = items.index(item)
            quantities[index] += quantity
            print(f"Added {quantity} more {item}(s).")
        else:
            items.append(item)
            quantities.append(quantity)
            print(f"Added new item: {item} ({quantity})")

    elif choice == '2':
        if not items:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for i in range(len(items)):
                print(f"- {items[i].capitalize()}: {quantities[i]}")

    elif choice == '3':
        item = input("Enter item name to remove: ").lower()
        if item in items:
            index = items.index(item)
            remove_qty = int(input("Enter quantity to remove: "))
            if remove_qty >= quantities[index]:
                items.pop(index)
                quantities.pop(index)
                print(f"All {item}s removed from inventory.")
            else:
                quantities[index] -= remove_qty
                print(f"{remove_qty} {item}(s) removed.")
        else:
            print("Item not found in inventory.")
    
    elif choice == '4':
        print("Exiting Inventory System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
