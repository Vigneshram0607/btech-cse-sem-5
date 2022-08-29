"""
input:
a c
1 3

ouput:
a1.a.1
a1.a.2
a1.a.3
a1.b.1
a1.b.2
a1.b.3
a1.c.1
a1.c.2
a1.c.3
a2.a.1
a2.a.2
a2.a.3
a2.b.1
a2.b.2
a2.b.3
a2.c.1
a2.c.2
a2.c.3
a3.a.1
a3.a.2
a3.a.3
a3.b.1
a3.b.2
a3.b.3
a3.c.1
a3.c.2
a3.c.3
b1.a.1
b1.a.2
b1.a.3
b1.b.1
b1.b.2
b1.b.3
b1.c.1
b1.c.2
b1.c.3
b2.a.1
b2.a.2
b2.a.3
b2.b.1
b2.b.2
b2.b.3
b2.c.1
b2.c.2
b2.c.3
b3.a.1
b3.a.2
b3.a.3
b3.b.1
b3.b.2
b3.b.3
b3.c.1
b3.c.2
b3.c.3
c1.a.1
c1.a.2
c1.a.3
c1.b.1
c1.b.2
c1.b.3
c1.c.1
c1.c.2
c1.c.3
c2.a.1
c2.a.2
c2.a.3
c2.b.1
c2.b.2
c2.b.3
c2.c.1
c2.c.2
c2.c.3
c3.a.1
c3.a.2
c3.a.3
c3.b.1
c3.b.2
c3.b.3
c3.c.1
c3.c.2
c3.c.3
S U C C E S S
"""
ch = input().split()
integer = input().split()
# print(ch)
# print(integer[0])
result = ""
c_list = []
for c in range(ord(ch[0]), ord(ch[1])+1):
    # print(chr(c))
    c_list.append(chr(c))
# print(c_list)
# count=0
for i in c_list:
    part_a_ch = i
    for j in range(int(integer[0]), int(integer[1])+1):
        part_a = part_a_ch + str(j)
        for b in c_list:
            part_b = b
            for c in range(int(integer[0]), int(integer[1])+1):
                part_c = str(c)
                result_c=part_a+"."+part_b+"."+part_c
                print(result_c)
                # count+=1

# print(count)
