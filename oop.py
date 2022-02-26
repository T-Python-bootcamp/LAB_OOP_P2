class peron :
    def __init__(self,name , age):
        self.name = name 
        self.age = age

    def display(self):
        print (f"name : {self.name} age : {self.age}")

class Student(peron):
    def __init__(self, name, age ,section) :
        self.section = section
        peron.__init__(self, name, age)

    def displayStudent(self):
                print (f"name : {self.name} age : {self.age}, section : {self.section}")  

############## test calss peron display method ##############

# person1 = peron( "rawan", 25) 
# print(person1)    
# person1.display()

############## test child class Student displayStudent method ##############

student1=Student ("rawan" ,25 ,"python")
print(student1)
student1.displayStudent()

####################################