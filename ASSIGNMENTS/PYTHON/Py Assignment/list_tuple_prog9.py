
stored_list = []
print("","NUMBERS WHICH ARE DIVISIBLE BY 7 AND NOT "
      "A MULTIPLE OF 5","", sep="*"*10)
for i in range(2000, 3201):
    if i%7 == 0 and i%5 !=0:
        print(i,end = " ")
        stored_list.append(i)

stored_tuple = tuple(stored_list)
print("\n\nSTORED TUPLE: ",stored_tuple)

