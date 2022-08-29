"""
10

8+2
[10 -- 1010
1*2^3=8
0*2^2=0
1*2^1=2
0*2^0=0,
8+2]

SUCCESS
"""
n = int(input())
n_ls=[]
ctr=0
for i in bin(n):
    n_ls.append(i)
    ctr+=1
# print(n_ls)
temp_ls = []
for i in n_ls:
    if i.isdigit():
        temp_ls.append(int(i)*(2**(ctr-1)))
    ctr-=1
temp_ls2=[]
for t in temp_ls:
    if t!=0:
        temp_ls2.append(t)
print(temp_ls2)
for _ in temp_ls2[:-1]:
    print(_,end='+')
print(temp_ls2[-1])



