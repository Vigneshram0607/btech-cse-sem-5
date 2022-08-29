"""
This module is used to get details of patient and Doctor
"""

#Importing Doctor Module
from doctor import doctor_details_insert
from doctor import doctor_details_input
from doctor import doctors_list

#Importing Patients Module
from patient import patient_details_insert
from patient import patient_details_input
from patient import patient_list,pat_display

#tp display menu
def command_menu():
    print("\nCOMMAND MENU")
    print("\nspec - List of All Patients Based On Specialization"
          "\nlist - List of All Patients"
          "\nadd - add Patient / Doctor"
          "\nexit - Exit Program"
          )

#to list patients
def list_pat():
    if len(patient_list) == 0:
        print("please fill list")
        # return "please fill list"
    else:
        i = 0
        for patient in patient_list:
            # print("{a}.{b}.".format(a=i , b=pat_display(patient_list[i][0])))
            pat_display(patient_list[i][0])
            # if len(patient_list)>=4:
            #     i += 4
            # else:
            #     break
            i+=1

#to add patient
def add_pat():
    patient_details_input()

#to add doctor
def add_doc():
    doctor_details_input()

#list based on specilisation
def list_spec_pat(spec_choice):
    j1 = 1
    j2=1
    if spec_choice == 'p':
        for i in range(len(patient_list)):
            if int(patient_list[i][1]) < 12:
                # for patient in patient_list:
                        # print("{ }.{ } .".format(j1, patient[0]))
                pat_display(patient_list[i][0])
                        # j1 += 1
    elif spec_choice == 'c':
        for i in range(len(patient_list)):
            if int(patient_list[i][1]) > 12:
                # for patient in patient_list:
                        # print("{ }.{ }.".format(j2, patient[0]))
                pat_display(patient_list[i][0])
                        # j2 += 1



#to invoke other module functions
def main():
    command_menu()
    while True:
        command = input("\nCommand: ").lower()
        if command == 'list':
            list_pat()
        elif command == "spec":
            spec_choice = input("Enter pediatrician or cardiologist [p/c]: ").lower()
            list_spec_pat(spec_choice)
        elif command == "add":
           add_choice = input("Patient or Doctor [p/d]: ").lower()
           if add_choice == 'p':
               add_pat()
           elif add_choice == 'd':
               add_doc()
           else:
               print("INVALID INPUT")
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("INVALID INPUT")

#invoke main function
if __name__ == '__main__':
    main()
