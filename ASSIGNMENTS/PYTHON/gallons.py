# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:11:03 2021

@author: Admin
"""
print("The MILES per Gallon Prog")
miles = float(input("ENter miles: "))
gas = float(input("ENter gas: "))
if miles >0 and gas>0:
    print(f"Miles per gallon: {miles/gas}")
else:
    print("Gallons used must be greater thean zero, please try again")
print("\nBye")
