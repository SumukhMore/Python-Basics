class Student: #class definition
    college_name = "ABC College" #class attribute

    def __init__(self, name, marks): #constructor
        self.name = name #object attribute / instance attribute
        self.marks = marks

    def welcome(self): #method definition
        print("Welcome", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Sumukh", 95) #object creation
s1.welcome()
print(s1.get_marks()) #calling method to get marks

# @staticmethod example 
class MathOperations:
    @staticmethod #static method definition
    def add(a, b): 
        return a + b
result = MathOperations.add(5, 10)
print(result)

# @staticmethod allows us to call the method without creating an instance of the class.# Methods example in Python OOP
