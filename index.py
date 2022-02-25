# - Create a child class Student  which inherits from the Person class and which also has a "section" attribute.
# - Create a method displayStudent() that displays the name, age and section.
# - Create a student object via an instantiation on the Student class and then test the displayStudent method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Your name is: {self.name}, And your age is: {self.age} years old."

class Student(Person):
    def __init__(self,name,age,section):
        self.section = section
        Person.__init__(self,name,age)

    def displayStudent(self):
        return f"Your name is: {self.name}, And your age is: {self.age} years old. And your section is: {self.section}"

firstStudent = Student('wala',25,'Python')

print(firstStudent.displayStudent())