n = int(input())
row = n**2
col = n**2

raw_matrix = [['-' for i in range(row)]for j in range(col)]
# print(raw_matrix)
for i in raw_matrix:
    print(*i)

for i in range(row):
    # print("i: ", i)
    for j in range(col):
        if j%n!=0 and i%n==0:
            raw_matrix[i][j] = '1'
            print("1-",i,j)
        elif j%n==0 and i%n!=0:
            raw_matrix[i][j] = '2'
            print("2-",i,j)
        # print("j: ",j)


print("RESULT")
for i in raw_matrix:
    print(*i)