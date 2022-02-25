
class personal:
    def __init__(self ,name ,age):
     self.name = name
     self.age =age 

    def display(self):
     print (f"welcom :{self.name} \n age :{self.age}")  
  
class  Student(personal):
 def __init__(self ,name ,age ,section):
    self.section = section 

    personal.__init__(self ,name ,age )
 
 def  displayStudent(self):

    print (f"welcom :{self.name} \n age :{self.age} \n  section : {self.section}")  
    
personals=personal( "jamelah", 25) 
print(personals)    
personals.display()
students=Student ("sara" ,25 ,"Computer Science")
students.displayStudent()
print(students)
        