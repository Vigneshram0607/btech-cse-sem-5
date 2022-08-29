"""
input:
49

output:
3

explanation:
4*9=36
3*6=18
1*8=8

input:
14

output:
1

explanation:
1*4=4
"""
#S U C C E S S

#TODO: get User input
num = int(input("Enter Number: "))
temp=0
first=0
second=0
count=0
# print(num//10)
# print(num/10)
# while num//10!=0:
#     first=num//10
#     second=num%10
#     num=first*second
#     count+=1



#
# result=1
# while num//10!=0:
#     # while num//10!=0:
#     while len(str(num))>1:
#         result = result*(num%10)
#         print("result: ",result)
#         num = num//10
#     num = result
#     count+=1
#     result=1
result=1
while num//10!=0:
    for i in range(len(str(num))):
        result = result*(num%10)
        num = num//10
    num = result
    count+=1
    result=1
print(count)