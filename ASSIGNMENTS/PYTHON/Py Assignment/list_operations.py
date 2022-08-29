import random
ls = []
res_ls = []
for i in range(20):
    ls.append(random.randint(1, 50))
# print(len(ls))
print("LIST: ",ls)
print("\nElements of the list that are less than 5: ")
for _ in ls:
    if _ <=5:
        print(_, end=' ')
        res_ls.append(_)

print("\n\nSTORED LIST: ",res_ls)
