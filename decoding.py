import random
import string
a="";b=""
char=string.ascii_letters+string.digits+string.punctuation
char1=string.ascii_letters+string.digits
for i in range(3):
    a+=random.choice (char)
print(a)
for i in range(3):
    b+=random.choice (char)
print(b)

f=open('C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\10hrs_lecture\\decode.txt','w')


f.write(input("Enter your secret message here  :  "))
f.close()
f=open('C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\10hrs_lecture\\decode.txt','r')
data=f.read()
f.close()
f=open('C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\10hrs_lecture\\decode.txt','w+')
data2=[]
data1=data.split()
for i in range(len(data1)):
    #print(data1[i][::-1],len(data1[i]))
    if len(data1[i])<=3:
        print(data1[i][::-1],end=" ", file=f) #reversing the string
    else:
        start=data1[i][0]
        middle=data1[i][1:]
        final=a+middle+start+b
        print(final,end=" ", file=f)
