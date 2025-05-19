amount = int(input("Enter the amount: "))

if amount >= 500:
    notes = amount//500
    print(f"500 x {notes} = 500") 
    amount =amount%500
if amount >= 200:
    notes = amount//200
    print(f"200 x {notes} = 200") 
    amount = amount % 200
if amount >= 100:
    notes = amount//100
    print(f"100 x {notes} = 100") 
    amount = amount % 100
if amount >= 50:
    notes = amount//50
    print(f"50 x {notes} = 50") 
    amount = amount % 50
if amount >= 10:
    notes = amount//10
    print(f"10 x {notes} = 10") 
    amount = amount % 10
if amount >= 5:
    notes = amount//5
    print(f"5 x {notes} = 5") 
    amount = amount % 5
if amount >= 2:
    notes = amount//2
    print(f"2 x {notes} = 2") 
    amount = amount % 2
if amount >= 1:
    notes = amount//1
    print(f"1 x {notes} = 1") 
    amount = amount % 1


