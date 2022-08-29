# n = 6478414
# k = 3 -digits
# output: largest int or -1

#S U C C E S S

n = int(input())
k = int(input())
ls = []
len_n = len(str(n))

if len(str(n)) >= k:
    for i in range(len(str(n))):
        if len(str(n)) >= k:
            # print("inside if")
            n_str = str(n)
            ls.append(n_str[-k: ])
            n = n//10
            print("n: ",n)
        else:
            break

    print(ls)
    for i in range(0, len(ls)):
        ls[i] = int(ls[i])
    # print(ls)
    ls.sort()

    print("Largest: ",ls[-1])
else:
    print("-1")