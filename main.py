


class Person:
    def __init__(self , name , age):
        self.name = str(name)
        self.age = int(age)
    
    def display(self):
        print(f"Name is: {self.name}")
        print(f"Age is : {self.age}")
    

class Student(Person):
    def __init__(self , name , age , section) :
        self.section = str(section)
    
        Person.__init__(self , name , age)

    def displayStudent(self):
        print(f"Name is: {self.name}")
        print(f"Age is : {self.age}")
        print(f"Section is :{self.section}")

a = Student("Mohammed" , 22 , "IT" )
a.displayStudent()