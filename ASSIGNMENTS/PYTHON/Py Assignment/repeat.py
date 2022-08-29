def rep_menu(r_menu):
    if r_menu == 1:
        print("\n", "STRING REPETATION", "", sep="\t" * 3)
        string_rep()
    elif r_menu == 2:
        print("\n", "LIST REPETATION", "", sep="\t" * 3)
        list_rep()
    elif r_menu == 3:
        print("\n", "TUPLE REPETATION", "", sep="\t" * 3)
        tuple_rep()
    elif r_menu == 4:
        print("\n", "NUMERIC REPETATION", "", sep="\t" * 3)
        num_rep()
    else:
        print("", "PLEASE CHECK UR INPUT", "", sep="*" * 10)
def string_rep():
    str1 = input("Enter a String to Perform Repetation: ")
    n = int(input("Enter How many times to Repeat: "))
    print(f"String Repetation of {str1} is '{str1*n}'")
def tuple_rep():
    t1 = []
    n = int(input("Enter How Many Times to Repeat: "))
    for i in range(1, 4):
        t1.append(int(input(f"Enter {i}th Element of Tuple: ")))
    t1 = tuple(t1)
    print(f"Repetation of Tuple{t1} is: {t1 * n}")
def list_rep():
    l1 = []
    n = int(input("Enter How Many Times to Repeat: "))
    for i in range(1, 4):
        l1.append(int(input(f"Enter {i}th Element of List: ")))
    print(f"Repetation of List{l1} is: {l1*n}")
def num_rep():
    num1 = input("Enter Numeric value to Repeat: ")
    n = int(input("Enter How many times to Repeat: "));print(f"Numeric Repetation of {num1} is :{num1*n}")
