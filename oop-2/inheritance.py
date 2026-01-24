class Car:
    color = "Black" 
    @staticmethod
    def start(): 
        print("Car started") 

    @staticmethod
    def stop():
        print("Car stopped")

class RangeRover(Car):
    def __init__(self, model):
        self.model = model

car1 = RangeRover("Autobiography")
car2 = RangeRover("Evoque")

print(car1.model)  # Output: Autobiography
print(car1.start())  # Output: Car started
print(car2.model)  # Output: Evoque
print(car2.stop())  # Output: Car stopped

# types of inheritance:
# Single Inheritance 
# Multi-level Inheritance
# Hierarchical Inheritance