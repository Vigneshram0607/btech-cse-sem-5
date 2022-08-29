
def con_menu(c_menu):
    if c_menu == 1:
        print("\n","STRING CONCATENATION","",sep="\t"*3)
        string_con()
    elif c_menu == 2:
        print("\n", "LIST CONCATENATION", "", sep="\t" * 3)
        list_con()
    elif c_menu == 3:
        print("\n", "TUPLE CONCATENATION", "", sep="\t" * 3)
        tuple_con()
    elif c_menu == 4:
        print("\n", "NUMERIC CONCATENATION", "", sep="\t" * 3)
        num_con()
    else:
        print("","PLEASE CHECK UR INPUT","",sep="*"*10)

def num_con():
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print(f"Numeric Concatenation of {num1} and {num2} is : {num1 + num2}")

def string_con():
    str1 = input("Enter String-1: ")
    str2 = input("Enter String-2: ")
    str3 = input("Enter String-3: ")
    str4 = str1 + str2 + str3
    print(f"String Concatenation: {str4}")



def tuple_con():
    t1 = []
    t2 = []
    for i in  range(1, 3):
        t1.append(int(input(f"Enter {i}th Element of First tuple: ")))
    for i in range(1, 3):
        t2.append(int(input(f"Enter {i}th Element of Second tuple: ")))
    t1 = tuple(t1)
    t2 = tuple(t2)
    print(f"Tuple Concatenation of {t1} and {t2}: {t1 + t2}")


def list_con():
    l1 = []
    l2 = []
    for i in range(1, 3):
        l1.append(int(input(f"Enter {i}th Element of First List: ")))
    for i in range(1, 3):
        l2.append(int(input(f"Enter {i}th Element of Second List: ")))
    print(f"List Concatenation of {l1} and {l2}: {l1 + l2}")