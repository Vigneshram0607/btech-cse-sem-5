# row_ls = []
# col_ls = []
# n = int(input())
# for i in range(n):
#     col_ls.clear()
#     for j in range(i+1):
#         col_ls.append('*')
#     row_ls.append(col_ls)
#
# for _ in row_ls:
#     print(_)

n,k=map(int,input().split())
l=[['*' for i in range(n)]for j in range(n)]
print(l)
for i in range(k-1,n-k+1): #n=5,k=1 - (0, 5):
    l[k-1][i]='#'
    l[i][k-1]='#'
    l[n-k][i]='#'
    l[i][n-k]='#'
for i in l:
    print(*i)