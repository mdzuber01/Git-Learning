#KBC CODE
questions=['Q1: Mount Everest is located in which country? ','Q2: What is value of pi? ','Q3: How many gf does khem have?']
answers=['d','d','a']
count=0
correctans=0
for q in questions:
    print(q)
    if count<1:
       print("Options:");
       print("A : China","B : India","C: America"," D: Nepal")
       ans=input("Please enter your answer among the options : ")
       if ans==answers[count]:
           print(" Correct Answer !!")
           correctans+=1
       else:
           print(" You choose wrong answer")
       
    if count>=1 and count<2:          
        print("Options:");
        print("A : 3.71","B : 1.43","C: 3.74"," D: 3.14")
        ans=input("Please enter your answer among the options : ")
        if ans==answers[count]:
            print(" Correct Answer !!")
            correctans+=1
        else:
            print(" You choose wrong answer")
    
    if count>=2:
       print("Options:");
       print("A : 0","B : 1","C: 3"," D: 2")
       ans=input("Please enter your answer among the options : ")
       if ans==answers[count]:
           print(" Correct Answer !!")
           correctans+=1
       else:
           print(" You choose wrong answer")
    count+=1
if correctans==len(questions):
    print(" !!.....Saat Crore.... !!...Huge Congratulations ...!!..Your all answers are corrects..!!")
elif correctans>=len(questions)-2:
    print(" Congratulation you won 3 crore")
else:
    print(" Try Next Time....!!!")
    