"""
abcdef
parcte

output:
YES
"""
"""
TRICK / TIPS:
s1,s2=input().strip().lower(),input().strip().lower()
if s1[::2] == s2[1::2] or s1[1::2] == s2[::2]:
    print('YES')
else: print('NO')
"""
s1 = input().lower()
s2 = input().lower()
# print(s1[::2])
# print(s2[1::2])
#
# print(s1[1::2])
# print(s2[::2])
#
# s1_odd = []
# s2_odd = []
# s1_even = []
# s2_even = []
#
# for i in range(0, len(s1)):
#     if i%2 != 0:
#         s1_odd.append(s1[i])
#         s2_odd.append(s2[i])
#     else:
#         s1_even.append(s1[i])
#         s2_even.append(s2[i])
#
# # print(s1_odd, s2_even)
# # print(s2_odd, s1_even)
#
# if (s1_odd == s2_even) or (s1_even == s2_odd):
#     print("YES")
# else:
#     print("NO")
