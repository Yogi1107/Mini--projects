n = int(input("Enter the number: "))
flag = False
for i in range(0,101):
    power = 2**i
    if n == power:
        print
        flag = True
        break
    else:
        flag = False

print(flag)        