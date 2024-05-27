"""dict={}
list=[]
for i in range(0,3):
    list.append(input(f"Enter the {i+1}th name :"))
dict["name"]=list
print(dict)
dict["new"]=dict
print(dict)"""
"""set1=set()
set1.add(int(9))
set1.add(float(9))
print("Set",set1)"""
import pandas as pd
dict={}

s1=input("Enter 1st subject name : ")
s2=input("Enter 2nd subject name : ")
s3=input("Enter 3rd subject name : ")
m1=float(input(f"Enter {s1} mark : "))
m2=float(input(f"Enter {s2} mark : "))
m3=float(input(f"Enter {s3} mark : "))
dict["Subject_wise_marks"]={s1:m1,s2:m2,s3:m3}
print(dict)
print("\nIN DATAFRAME\n",pd.DataFrame(dict.values(),index=['1']))