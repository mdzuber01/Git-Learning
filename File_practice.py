#I/O Practice
with open("practice.txt","w") as f:
    f.write("Hi everyone\n we are learning File I/O\nusing Java.\n I like programming in Java")
with open("practice.txt","r") as f:
    data=f.read()
    #print(data)
    new_data=data.replace("Java","Python")
    #print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)
#Function to check inputed word exits in a file or not.  
def check(word):
    with open("practice.txt","r")as f:
        data=f.read()
        if data.find(word)!=-1:
            #s=open("practice.txt","w")
            print("\nsearched word exists")#,file=s)  #To append "searched word exists" in practice.txt file.
        else:
            print("Not Exists..!!")
check("lbearning")      
            
           
        

