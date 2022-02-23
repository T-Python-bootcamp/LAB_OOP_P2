class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self, name, age, section):
        self.section = section
        Person.__init__(self, name, age)

    def displayStudent(self):
        print(self.name)
        print(self.age)
        print(self.section)
studentObject = Student("Mohmmad", 24, "A")
studentObject.displayStudent()