import csv

FILENAME = 'employee.csv'

def write_employee(employees):
    with open(FILENAME,'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(employees)

def read_employee():
    emp = []
    with open(FILENAME,'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            emp.append(row)
    return emp

def list_employees(employees):
    for i in range(1, len(employees)):
        emp = employees[i]
        print(str(i) + ". EMP ID: "+emp[0]+"\tNAME: "+emp[1]+"\tEMAIL ID: "+emp[2]+"\tNUMBER: "+emp[3]+"\tHIRE-DATE: "+emp[4]+"\tSALARY: "+emp[5]+"\tMANAGER-ID: "+emp[6]+"\tDEPT-ID: "+emp[7])
    print('\n')

def add_employee(employees):
    emp = []
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    email = input("Email ID: ")
    ph_num = input("Phone Number: ")
    hire_date = input("Hire Date: ")
    salary = input("Salary: ")
    manager_id = input("Manager ID: ")
    dept_id = input("Department ID: ")
    emp.append(emp_id)
    emp.append(name)
    emp.append(email)
    emp.append(ph_num)
    emp.append(hire_date)
    emp.append(salary)
    emp.append(manager_id)
    emp.append(dept_id)
    employees.append(emp)
    write_employee(employees)
    print(name+" was added.\n")

def del_employee(employees):
    index = int(input("Number: "))
    if index>=1:
        emp = employees.pop(index)
        write_employee(employees)
        print(emp[1]+" was deleted.\n")
    else:
        print("UNABLE TO DELETE")

def search_employee(employees):
    name_search = input("Name: ")
    found = False
    for emp in employees:
        if name_search.lower() == emp[1].lower():
            print("Succesfully Found "+name_search)
            found = True
            print("EMP ID: " + emp[0] + "\tNAME: " + emp[1] + "\tEMAIL ID: " + emp[2] + "\tNUMBER: " + emp[3] + "\tHIRE-DATE: " + emp[4] + "\tSALARY: " + emp[5] + "\tMANAGER-ID: " + emp[6] + "\tDEPT-ID: " +emp[7])
    if not found:
        print("EMPLOYEE NOT FOUND")


def menu():
    print("\nCOMMAND MENU")
    print("list - LIST EMPLOYEES.")
    print("add - ADD EMPLOYEES.")
    print("del - DELETE EMPLOYEES.")
    print("search - SEARCH EMPLOYEES.")
    print("exit - EXIT.")
    print('\n')


def main():
    print("Employee List Program")
    menu()
    emp_list = read_employee()
    while True:
        command = input('COMMAND: ').lower()
        if command == 'list':
            list_employees(emp_list)
        elif command == 'add':
            add_employee(emp_list)
        elif command == 'del':
            del_employee(emp_list)
        elif command == 'search':
            search_employee(emp_list)
        elif command == 'exit':
            print('\nBye.')
            break
        else:
            print("INVALID INPUT")

if __name__ == '__main__':
    main()


