"""
This module is meant for updating Patients details in list

patient - Name, Age, weight & Mobile_Number
"""


patient_list = [] #list definition

#to insert into list
def patient_details_insert(data):
    patient_list.append(data)

#to get user input
def patient_details_input():
    print("\n\nEnter the Appropriate Patient details\n\n")
    pat_name = input("Enter Patient's Name: ")
    # patient_details_insert(pat_name)
    pat_age = input("Enter Patient's Age: ")
    # patient_details_insert(pat_age)
    pat_weight = input("Enter Patient's Weight: ")
    # patient_details_insert(pat_weight)
    pat_num = input("Enter Patient's Mobile Number: ")
    # patient_details_insert(pat_num)
    # patient_list.append(data)
    data = [pat_name, pat_age, pat_weight, pat_num]
    patient_details_insert(data)

#to display list data
def pat_display(patientList):
    print(patientList)