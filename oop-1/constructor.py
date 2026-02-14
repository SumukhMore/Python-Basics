class Student: # Define a class named Student

    def __init__(self, fullname): # Constructor method to initialize the object
        self.name = fullname 
        print("Adding Student:") 

student1 = Student("Sumukh") # Create an instance of the Student class
print(student1.name) 

student2 = Student("Ananya") # Create another instance of the Student class
print(student2.name)# Constructor example in Python OOP
