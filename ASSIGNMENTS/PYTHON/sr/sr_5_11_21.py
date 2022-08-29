"""
4

1
1 1 2
1 1 2 1 2 3
1 1 2 1 2 3 1 2 3 4

SUCCESS
"""
n = int(input())
ctr=1
first = []
temp_first = []
for i in range(n):
    temp_ctr=1
    if i==0:
        print(i+1)
        temp_first.append(i+1)
        # first.append(temp_first)
        # print(first)
    else:
        for _ in first[i-1]:
            print(_,end=' ')
            temp_first.append(_)
        for j in range(1, i+1+1):
            print(j, end=' ')
            temp_first.append(j)
        print()
    first.append(temp_first)
    temp_first=[]
    # print(first)






