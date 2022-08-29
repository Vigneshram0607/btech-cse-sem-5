from datetime import datetime, timedelta

def main():
    print("The Invoice Due date program\n")
    while True:
        invoice_date = input("\nEnter the invoice date (MM/DD/YY): ")
        # print(invoice_date_str)
        if '/' not in invoice_date:
            print("INVALID DATE FORMAT! Please Check Your FORMAT")
            break
        else:
            invoice_date = datetime.strptime(invoice_date, "%m/%d/%Y")

        due_date = invoice_date + timedelta(days=30)
        current_date = datetime.now()
        days_overdue = (current_date - due_date).days # display results
        print("Invoice Date: " + invoice_date.strftime("%B %d, %Y"))
        print("Due Date: " + due_date.strftime("%B %d, %Y"))
        print("Current Date: " + current_date.strftime("%B, %Y"))
        if days_overdue > 0:
            print("This invoice is", days_overdue, "day(s) overdue.")
        # elif days_overdue<0:
        #     print("Invoice date must not be earlier")
        else:
            days_due = days_overdue * -1
            print("This invoice is due in", days_due, "day(s).")

        result = input("Continue? (y/n): ")

        if result. lower() != "y":
            break


if (__name__ == "__main__"):
    # print("HI")
    main()
    print("Bye!")

