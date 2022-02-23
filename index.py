
class Person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def display(self):
        print(f'name is {self.name} ,age is {self.age}')
class Student(Person):
    def __init__(self, name, age,section):
        self.section=section
        Person.__init__(self,name, age)
    def display(self):
        print(f'name is {self.name} ,age is {self.age},section is {self.section}')
student1=Student("sara",20,"IT")
student1.display()