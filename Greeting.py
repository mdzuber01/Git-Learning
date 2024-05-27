# Write a program to greet someone.
import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
name=input("Enter you name please : ")
hour=int(time.strftime('%H'))
#hour=int(input("Enter a number"))
if hour>=0 and hour<13:
    print(" Good Morning ", name)
elif hour>=13 and hour<19:
    print(" Good Afternoon ", name)
else:
    print(" Ghar jaau ",name, " dherai dhilo vayo")