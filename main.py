
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: {name}\nAge: {age}".format(age=self.age,name=self.name))

class Student(Person):
    def __init__(self, name, age,section):
        super().__init__(name, age)
        self.section=section
    def displayStudent(self):
        self.display()
        print(f"Section: {self.section}")

s1 = Student("Ahmed",25,442)
s1.displayStudent()
