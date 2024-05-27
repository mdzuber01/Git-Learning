with open("practice1.txt","w+") as f:
    f.write("Hi everyone\n we are learning File I/O\nusing Java.\n I like programming in Java")
    f.seek(0)
    data=f.read()
    print(data)
    f.seek(0)
    new_data=data.replace("Java","Python")
    f.write(new_data)
    f.seek(0)
    print(f.read())
def check(word):
    with open("practice1.txt","r")as f:
        data=f.read()
        if data.find(word)!=-1:
            #s=open("practice.txt","w")
            print("\nsearched word exists")#,file=s)  #To append "searched word exists" in practice.txt file.
        else:
            print("Not Exists..!!")
check("lbearning")      
