# ch='a'
# print(ord(ch))

# for i in range(1,1001):
#     num = i
#     sum1=0
#     n=len(str(i))
#     while num!=0:
#         digit = num % 10
#         sum1 += digit**n
#         num = num //10
#     if(sum1==i):
#         print(    

string = 'Kiran'
for i in range(len(string)-1,-1,-1):
    print(string[i],end="")
print()