# function based way
#def abc():
   # name=input("Enter a name")
    #age=input("Enter age")
   # print(name)
    #print(age)
#abc()
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def get_data(self,name, age):
        self.name=name
        self.age=age
    def put_data(self):
        print(self.name)
        print(self.age)
student1=Student("","")

name=input("Enter name")
age=input("Enter age")
student1.get_data(name, age)
student1.put_data()