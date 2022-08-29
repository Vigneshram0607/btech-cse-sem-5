"""
google

g2 o2 o1 g1 l1 e1

SUCCESS
"""

str_ip = input()
str_ls = []
for i in str_ip:
    str_ls.append(i)
# str_ls = str_ip.split()
print(str_ls)
# print(str_ls.count('g'))

temp_ls = []
for i in str_ls:
    if i in temp_ls:
        print(f'{i}{str_ls.count(i) - temp_ls.count(i)}')
        temp_ls.append(i)
    else:
        print(f'{i}{str_ls.count(i)}')
        temp_ls.append(i)