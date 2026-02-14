class Student:
    def __init__ (self, name):
        self.name = name

s1 = Student("Sumukh")
print(s1) # Output: <__main__.Student object at ...>
print(s1.name)  # Output: Sumukh
del s1 # Deleting the object reference
print(s1)  # This will raise a NameError since s1 has been deleted# Delete object example in OOP
