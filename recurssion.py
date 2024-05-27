#WAP to take a number as a input from the user, and return string ODD or EVEN if the entered number is odd or string respectively.

"""def zub(num):
    if num % 2==0: 
        print("even",str(num))
    else:
        print("odd",str(num))
zub(int(input("Enter any number : ")))"""
#recursion
"""
#.....print sum of n numbers

def sum(num):
    if(num==0):
        return 0
    else:
        return (num+sum(num-1))
        
print(sum(int(input("Enter any number : "))))"""

# write a recursive function to print all the elements in a list.
idx=0
def b(list,idx):
    a=len(list)
    if idx==a:
        return
    else:
        print(list[idx],end="-")
    idx+=1
    b(list,idx)
list=["Zuber","MD","UMN","IOE"]
b(list,idx)