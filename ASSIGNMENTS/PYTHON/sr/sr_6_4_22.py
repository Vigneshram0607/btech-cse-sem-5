str = input("enter: ")
print("Str ",str)
temp_str = ""
# temp_i=0
for i in str:
    c = temp_str.count(i)
    print("c: ",c)
    print("i: ",i)
    temp_i=0
    while(c!=0):
        temp_i = ord(i) + 1
        print("temp_i: ",temp_i)
        print("chr(temp_i): ",chr(temp_i))
        c = c-1
    i = chr(temp_i)
    print("i2: ",i)
    print("temp_i: ", temp_i)
    print("chr(temp_i): ", chr(temp_i))
    temp_str+=i
print(temp_str)

# currentaffairs