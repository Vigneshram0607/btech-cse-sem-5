"""
3
15 10 8

op:
9

ex:
15>>1 = 7
10>>1 = 2
8>>1 = 0
7+2+0 = 9
"""

# Function to turn off k'th bit in `n`
def turnOffKthBit(n, k):
	return n & ~(1 << (k - 1))


n = int(input())
n_ls = map(int, input().split())
print(n)
count=0
# for i in n_ls:
#     # print(i, i>>1)
#     # print(i,i>>(2**count))
#     # sum+=i>>(2**count)
#     # count+=1
#     sum += i & ~(1 >> (3))
#     print(sum,i)
# print(sum)

off_bit = []
for i in n_ls:
    a = turnOffKthBit(i, 4)
    off_bit.append(a)
    print(a)
for i in off_bit:
    print(i)
print(sum(off_bit))