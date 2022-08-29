"""
4
4647 67865 150 321879
"""
n = int(input())
n_ls = input().split()
# for i in range(0,n):
#  n_ls[i] = int(n_ls[i])
result_ls = []

for n_i in n_ls:
 result = ""
 for int_i in  range(9,-1,-1):
  if str(int_i) not in n_i:
   result+=str(int_i)
 result_ls.append(result)

result_sum=0
for i in result_ls:
 result_sum += int(i)
print(n)
print(n_ls)
print(result_ls)
print(result_sum)