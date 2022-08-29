# n = int(input())
# input_list = []
# jars_list = []
# lids_list = []
# input_str = input( )
# input_list = input_str.split()
# for i in input_list:
#     # insert_n = int(input(" "))
#     # input_list.append(insert_n)
#     if int(i)%2 == 0:
#
#         jars_list.append(int(i))
#     elif int(i)%2!=0:
#         lids_list.append(int(i))
# print(input_list)
# print("jars_list: ",jars_list)
# print("lids_list: " ,lids_list)
#
# if len(jars_list) == len(lids_list):
#     print(len(jars_list)-1)

#F A I L

jarandlid = int(input())
jarandlidlist = input().split()
jarlist = []
lidlist = []
count = 0

for val in jarandlidlist:
    val = int(val)
    if val % 2 == 0:
        lidlist.append(val)
    else:
        jarlist.append(val)

print(lidlist, jarlist)
for val in jarlist:
    if int(val) + 1 in lidlist:
        count += 1
        lidlist.remove(int(val) + 1)
print(count)