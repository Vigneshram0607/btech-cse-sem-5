import random
def remove_duplicates(data):
    no_dup = []
    for element in data:
        if element not in no_dup:
            no_dup.append(element)
    return no_dup
tuple_data = ()
list_data = []
for i in range(10):
    tuple_data+=(random.randint(1, 100),)
    list_data.append(random.randint(1, 100))

tuple_data_list = list(tuple_data)
print(f"\n\nTUPLE DATA: {tuple_data}")

dup_tuple = []
dup_list = []
for i in tuple_data_list:
    if tuple_data_list.count(i)>=2:
       dup_tuple.append(i)

dup_tuple = remove_duplicates(dup_tuple)
# print(dup_tuple)

tuple_len = len(tuple_data)
list_len = len(list_data)

if tuple_len%2==0:
    median_cal = (tuple_len)//2
else:
    median_cal = (tuple_len+1)//2

if list_len%2==0:
    median_cal_list = (list_len)//2
else:
    median_cal_list = (list_len+1)//2
print(f"Average = {sum(tuple_data)//len(tuple_data)} "
      f"Median = {tuple_data_list[median_cal-1]} "
      f"Min = {min(tuple_data)} "
      f"Max = {max(tuple_data)} "
      f"dups[] = {dup_tuple}")
for j in list_data:
    if list_data.count(j)>=2:
         dup_list.append(j)

dup_list = remove_duplicates(dup_list)
# print(dup_list)
print(f"\n\nRANDOM DATA: {list_data} ")
print(f"Average = {sum(list_data)//len(list_data)} "
      f"Median = {list_data[median_cal_list-1]} "
      f"Min = {min(list_data)} "
      f"Max = {max(list_data)} "
      f"dups[] = {dup_list}")