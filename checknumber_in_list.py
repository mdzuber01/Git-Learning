"""i=1
target=81
list=[]
while i<=10:
    list.append((i)**2)
    i+=1
print(list)
i=1
while target!=list[i-1]:
    i+=1
print("Our Target number is ", list[i-1])"""
k=1
target=int(input("Enter a number you want to search in a list : "))
list=[1,4,9,16,25,36,49,64,81,100]
while True:
    i=1;j=0
    while i <= len(list):
        if target!=list[i-1]:
            i+=1 
            j+=1
        else:
            print(f"{list[i-1]} is your searched number with index{i-1}, and you find it in a {k} attempt")
            print("\n !!...MISSION COMPLETED...!!")   
            break
        
    if j==len(list):
        print("Number not found !!")
        target=int(input("Enter any other number : "))
        k+=1
    else:
        break
        

    
