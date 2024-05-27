import pandas as pd
class practice:
    def __init__(self,name,roll_no,age,marks):
        self.name=name
        self.roll=roll_no
        self.age=age
        self.marks=marks
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Roll no : ", self.roll)
        print(" Marks in each subject \n: ",pd.DataFrame(self.marks,index=['a']))
a=practice("MD Zuber","080", 25, {'phy':93,'Maths':97,'Applied Mechanics':89})
a.display()

