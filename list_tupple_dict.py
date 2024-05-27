"""list=[]
name1=input("Enter the 1st Movie name : ")
list.append(name1)
name2=input("Enter the 1st Movie name : ")
list.append(name2)
name3=input("Enter the 1st Movie name : ")
list.append(name3)
print("The list of 3 Movies is presented below\n  ",list)
print(name1+" "+name2+" "+name3)"""
"""list=[2,3,5,5,3,4]
list1=list.copy()
list1.reverse()
if list1==list:
    print("List ha Palindrome element")
else:
    print("List has not palindrome element")
print(list1)"""
"""tup=("C","D","A","A","B","B","A")
countA=tup.count("A")
print(f"The value of A appear {countA} times in tuple :{tup}")
list=[]
for i in range(0,len(tup)):
    list.append(tup[i])
print(list)
#sorteded=sorted(list)
list.sort()
print("Sorted:",list)
#print(sorteded)"""
"""import pandas as pd
dict={"name":["MD Zuber","Bhakti Lekhak"],"age":[25,24],"sex":["Male","Female"]}
dict["phone"]=[9815784967,9868806849]
dict.update({"Grade":['A+','A+']})
#Add a new data i.e, phone as a key value and phone number as a data.
#print(dict["name"],dict["sex"])
print(dict,len(dict))
print("    \nDictionary in DataFrame using Pandas library\n\n",pd.DataFrame(dict))
print(dict.get("Grade"))#return the values in key Grade
#print(pd.Series(dict["name"],index=['a','b']))
#print(len(list(dict.keys())),dict.values(),dict.items())"""
list=["python",'java','c++','python','javascript','java','python','java','c++','c']
print(list)
a=set()
for i in range(0,len(list)):
    a.add(list[i])
print("The number of class required is :",len(a))
    
