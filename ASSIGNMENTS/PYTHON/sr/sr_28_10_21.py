"""
FOR ME IT IS SUCCESSS

"""

str_ip = input()
ch, x = input().split()
x = int(x)
first = str_ip[:x-1]
second = str_ip[x-1:]
# print("FIRST: ",first,second)
reverse_1 = first[::-1]
reverse_2 = second[::-1]
# print("REV: ",reverse_1, reverse_2)
print(len(str_ip))
print(len(first))
print(len(reverse_2))
largest=smallest=0
if len(first)>=len(reverse_2):
    largest = first
    smallest = reverse_2
else:
    largest = reverse_2
    smallest = first

if ch.lower() == 'u':
    # print(ch)
    print("",reverse_2,sep='*'*(len(largest)-len(smallest)))
    print(first)
elif ch.lower() == 'd':
    # print(ch)
    print("",first,sep='*'*(len(reverse_2)-len(first)))
    print(reverse_2)



