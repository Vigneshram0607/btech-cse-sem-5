"""
ip-1:
4
3
10 30 60
+ - 70
20 95 +
25 50 10

op:
10 30 60
30 65 70
20 95 80
25 50 10

ip-2:
6
6
6 7 3 8 3 7
- 3 9 + 5 1
6 - 9 5 - -
4 6 3 + 4 3
- + 9 7 + +
1 5 7 6 3 7

op:
6 7 3 8 3 7
0 3 9 13 5 1
6 3 9 5 1 2
4 6 3 12 4 3
3 11 9 7 7 10
1 5 7 6 3 7
S U C C E S S
"""
n = input().split()
row = int(n[0])
col = int(n[1])
a=[]
for i in range(row):
    a.append(input().split())

for i in range(row):
    for j in range(col):
        # print(a[i][j],end='.')
        if a[i][j]=='+':
            a[i][j] = int(a[i-1][j])+int(a[i+1][j])
            # print(a[i][j])
        elif a[i][j]=='-':
            a[i][j] = int(a[i-1][j])-int(a[i+1][j])
            if a[i][j]<0:
                a[i][j]*=-1
        print(a[i][j], end=' ')
    print()
