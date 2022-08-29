"""
PASCAL TRIANGLE
"""

n = int(input()) #num of integers
given_ls = list(map(int, input().split()))
row_to_find = given_ls[1]
list1=[] #list to store pascal triangle

# tri_ls = [[1],[1,1]]
# for i in range(2, row_to_find+1):
#     for j in range(i):
#         if j==0 or j==i:
#             tri_ls[i][j] = 1
#         else:
#             tri_ls[i][j] =

#TODO: CODE TO BUILD PASCAL TRIANGLE:
for i in range(row_to_find+1):
  list1.append([])
  list1[i].append(1)
  for j in range(1, i):
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
  if(row_to_find != 0):
    list1[i].append(1)

print(list1)
for i in list1[row_to_find]:
  print(i, end=" ")
