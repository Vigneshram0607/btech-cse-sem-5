"""
XOR
4
1 2 3 4

1^2 2^3 3^4
"""
n = int(input())
init_ls =input().split()
print(init_ls)
final = []
copy_ls = init_ls
temp_ls = []
temp_len = n
for i in range(temp_len-1):
    temp_ls.append(copy_ls[i]^copy_ls[i+1])
