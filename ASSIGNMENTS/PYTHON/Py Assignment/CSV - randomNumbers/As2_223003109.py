import csv, random

FILENAME = 'your_filename.csv'
final_ls = []
temp_ls = []
count=0
while True:
    rand_num = random.randint(100, 999)
    if rand_num not in final_ls:
        final_ls.append(rand_num)
        count+=1
    if count==899:
        break
# print(len(final_ls))
try:
    with open(FILENAME, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(final_ls)
except FileNotFoundError:
    print("file not found")
except:
    print('UNKNOWN EXCEPTION')

with open(FILENAME,'r') as read_file:
    data = csv.reader(read_file)
    for i in data:
        print(*i)

