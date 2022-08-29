# from datetime import *
# date_ip = input("enter date (MM/DD/YYYY): ")
# # print("Your input: ",date_ip)
# crct_date = datetime.strptime(date_ip, "%m/%d/%Y")
# print("DATE: ",crct_date)
#
#
# from datetime import datetime, timedelta
#
# is_crct = True
#
# def get_invoice_date():
#     invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")
#     if '/' not in invoice_date_str:
#         is_crct = False
#     invoice_date =datetime. strptime (invoice_date_str, "%m/%d/%Y")
#     return invoice_date
#
# def main():
#     print("The Invoice Due Date program")
#     print()
#     while is_crct:
#         invoice_date = get_invoice_date()
#         print() # calculate due date and days overdue
#         due_date = invoice_date + timedelta(days=30)
#         current_date = datetime.now()
#         days_overdue = (current_date - due_date).days # display results
#         print("Invoice Date: " + invoice_date.strftime("%B %d, %Y"))
#         print("Due Date: " + due_date.strftime("%B %d, %Y"))
#         print("Current Date: " + current_date.strftime("%B, %Y"))
#         if days_overdue > 0:
#             print("This invoice is", days_overdue, "day(s) overdue.")
#         else:
#             days_due = days_overdue * -1
#             print("This invoice is due in", days_due, "day(s).")
#         print() # ask if user wants to continue
#         result = input("Continue? (y/n): ")
#         print()
#         if result. lower() != "y":
#             print("Bye!")
#             break
#
# # if __name__ == "__main__":
# main()

from datetime import datetime, timedelta


def stringmat(str):
    if ('/' in str[0:3] and str[0:2].isdigit()):
        if ('/' in str[0:3] and str[3:5].isdigit()):
            if ('/' in str[0:3] and str[6:8].isdigit()):
                return True
    else:
        return -1


def get_invoice_date():
    invoice_date_str = input("Enter the invoice date (MM/DD/YY):")
    print(stringmat(invoice_date_str))


def main():
    print("The Invoice Due date program")
    print()

    while True:
        get_invoice_date()
        print()


if (__name__ == "__main__"):
    # print("HI")
    main()
