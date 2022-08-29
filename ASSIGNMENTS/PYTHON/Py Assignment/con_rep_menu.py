from concatenate import *
from repeat import *




def concatenation_menu():
    print("\nCONCATENATION MENU:\n1.String Concatenation.\n"
          "2.List Concatenation.\n"
          "3.Tuple Concatenation.\n"
          "4.Numeric Concatenation.")
    c_menu = int(input("Enter Number to Perform OPERATION: "))
    con_menu(c_menu)

def Repetation_menu():
    print("\nREPETATION MENU:\n1.Repetation On Strings.\n"
          "2.Repetation On List.\n"
          "3.Repetation On Tuple.\n"
          "4.Repetation on Numbers.")
    r_menu = int(input("Enter Nunmber to Perform OPERATION: "))
    rep_menu(r_menu)

is_again = True
while is_again:
    c_or_r = input("Enter 'c' for CONCATENATION, 'r' for REPETATION [c/r]: ").lower()

    if c_or_r == 'c':
        concatenation_menu()
    elif c_or_r == 'r':
        Repetation_menu()
    else:
        print("","INVALID INPUT","",sep = "*"*20)
    if input("Contiue [y/n]: ").lower() == 'n':
        print("\n\nBye!")
        is_again = False