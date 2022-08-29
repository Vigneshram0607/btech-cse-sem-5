"""
This module is used to update Doctors details in list.
"""

doctors_list = [] #list definition

#to insert into list
def doctor_details_insert(data):
    doctors_list.append(data)

#to get user input
def doctor_details_input():
    print("\n\nEnter the Appropriate Doctor details\n\n")
    doc_name = input("Enter Doctor's Name: ")
    doctor_details_insert(doc_name)
    doc_spec = input("Enter Doctor's Specialization: ")
    doctor_details_insert(doc_spec)
