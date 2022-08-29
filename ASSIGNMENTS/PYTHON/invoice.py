# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:25:42 2021

@author: Admin
"""

print("The INVOICE prog")

cust_type = input("ENter cust type(r/w): ").lower()
inv = float(input("TOT INVOICE: "))
disc=0
if cust_type == 'r':
    if inv<100:
        disc += 0
    elif inv>=100 and inv<250:
        disc += 0.1
    elif inv>=250:
        disc+=0.2
elif cust_type=='w':
    if inv<500:
        disc+=0.4
    elif inv>=500:
        disc+=0.5
print("Invoice Total:\t\t",inv)
print("Discount Percent:\t",disc)
print("Discount Amount:\t",disc*inv)
print("New Invoice Total:\t",inv - (inv*disc))