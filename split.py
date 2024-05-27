string="1,2,3,4,5,6"
list=string.split(",");count=0
"""for val in list:
    if int(val)%2==0:
        count+=1
        print(int(val))
print(count)"""
for i in range(len(list)):
    if int(list[i])%2==0:
        count+=1
        print(int(list[i]))
print("Done",count)
