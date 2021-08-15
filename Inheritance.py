class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def get_data(self):
        self.name=input("Enter name:")
        self.age=input("Enter age:")

    def put_data(self):
        print(self.name)
        print(self.age)

class ScienceStudent(Student):
    def science(self):
        print("This a science method")
        
a=ScienceStudent("","")
a.get_data()
