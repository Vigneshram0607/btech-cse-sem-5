import csv

FILENAME = 'scores.csv'

def list_data(students):
    for i in range(1, len(students)):
        student = students[i]
        print(str(i)+
              ".STUD ID: "+str(student[0])+
                  "\tSTUD NAME: "+student[1]+
                  "\tM1: " + str(student[2]) +
                  "\tM2: " + str(student[3]) +
                  "\tM3: " + str(student[4]) +
                  "\tM4: " + str(student[5]) +
                  "\tM5: " + str(student[6]) +
                  "\tTOTAL: " + str(student[7]) +
                  "\tAVERAGE: " + str(student[8])
                  )

def search_student(students):
    name_search = input("Name: ")
    found = False
    for student in students:
        if name_search.lower() == student[1].lower():
            print("SUCCESSFULLY FOUND "+name_search)
            found = True
            print(
                  "STUD ID: "+student[0]+
                  "\tSTUD NAME: "+student[1]+
                  "\tM1: " + student[2] +
                  "\tM2: " + student[3] +
                  "\tM3: " + student[4] +
                  "\tM4: " + student[5] +
                  "\tM5: " + student[6] +
                  "\tTOTAL: " + student[7] +
                  "\tAVERAGE: " + student[8]
                  )
    if not found:
        print("STUDENT NOT FOUND")

def calc_tot_avg(total):
    return round(total/5, 2)

def write_student(students):
    student = []
    stud_id = input("Student ID: ")
    stud_name = input("Student Name: ")
    m1 = int(input("M1: "))
    m2 = int(input("M2: "))
    m3 = int(input("M3: "))
    m4 = int(input("M4: "))
    m5 = int(input("M5: "))
    total = m1+m2+m3+m4+m5
    avg = calc_tot_avg(total)
    student.append(stud_id)
    student.append(stud_name)
    student.append(m1)
    student.append(m2)
    student.append(m3)
    student.append(m4)
    student.append(m5)
    student.append(total)
    student.append(avg)
    students.append(student)
    try:
        with open(FILENAME,'w') as write_file:
            writer = csv.writer(write_file)
            writer.writerows(students)
    except FileNotFoundError:
        print("FILE NOT FOUND, please check the File Name")
    except Exception:
        print("Sry, UNKNOWN EXCEPTION while Writing.")
    print(stud_name+" was Successfully added.\n")

def read_student():
    stud = []
    try:
        with open(FILENAME,'r') as read_file:
            reader = csv.reader(read_file)
            for row in reader:
                stud.append(row)
    except FileNotFoundError:
        print("FILE NOT FOUND, please check the File Name")
    except Exception:
        print("Sry, UNKNOWN EXCEPTION")
    return stud

def menu():
    print("\nCOMMAND MENU")
    print("list - display all scores.")
    print("add - add new student score record.")
    print("search - fetch a student score record.")
    print("exit - EXIT.")
    print('\n')

def main():
    print('Student Score Program')
    menu()
    stud_list = read_student()
    while True:
        command = input('\nCOMMAND: ').lower()
        if command == 'list':
            list_data(stud_list)
        elif command == 'add':
            write_student(stud_list)
        elif command == 'search':
            search_student(stud_list)
        elif command == 'exit':
            print('\nBye.')
            break
        else:
            print("INVALID INPUT")

if __name__ == '__main__':
    main()