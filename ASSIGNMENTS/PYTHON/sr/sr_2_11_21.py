n = int(input())
pairs = []
for i in range(n):
    temp_ls = input().split()
    pairs.append(temp_ls)
# for i in pairs:
#     print(i)
clock_matrix = [['*' ,'11', '12', '1' ,'*'],
['10' ,'*' ,'*' ,'*' ,'2'],
['9', '*' ,'*' ,'*' ,'3'],
['8', '*', '*', '*', '4'],
['*' ,'7', '6', '5', '*']]
for pair_row in pairs:
    for clk_row in clock_matrix:
        if pair_row[0] in clk_row or pair_row[1] in clk_row:
            for i in range(len(clk_row)):
                if clk_row[i] == pair_row[0]:
                    clk_row[i] = pair_row[1]
                    print(f'\t1\t{clk_row}')
                elif clk_row[i] == pair_row[1]:
                    clk_row[i] = pair_row[0]
                    print(f'\t2\t{clk_row}')
    print('\n\n\n\n')
    print(pair_row)
    for c in clock_matrix:
        print(c)
print('\n\n\n\n')
for c in clock_matrix:
    print(*c)




