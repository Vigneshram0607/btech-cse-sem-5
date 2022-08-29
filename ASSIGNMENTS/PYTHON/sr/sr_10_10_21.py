"""
INPUT:
10 [NUM OF EMPLOYEES]
500 [C]
3 [NUM OF DAYS]

OUTPUT:
501 502 503 ... 510
 F A I L
"""

emp = int(input())
c = int(input())
days = int(input())

total_list = []
temp_list = []
# total_list.append(temp_list)
# print(temp_list[0])
# for _ in range(days):
#     temp_list.insert(_, 0)

for e in range(1, 1+emp):
        temp_list.append(c+e)
print("1: ",temp_list)
total_list.append(temp_list)
print("1: ",total_list)
for day in range(2, days+1):
    for e in range(1, 1+emp):
        temp_list.insert(e-1, total_list[day-2][e-1]+c+(day-1))
        print("total_list[day-2][e-1]: ",total_list[day-2][e-1])
        # temp_list.append()
        # temp_list.append(c+e)
    print(temp_list)
    total_list.insert(day, temp_list)
    # temp_list.clear()
print(total_list)