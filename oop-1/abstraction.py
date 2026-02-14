class Car:
    def __init__(self):
        self.acc = False  # Private attribute
        self.brk = False  # Private attribute
        self.clutch = False  # Private attribute

    def press_accelerator(self):
        self.acc = True
        self.brk = False
        self.clutch = False
        print("Accelerating")

car1 = Car()
car1.press_accelerator()

# Abstraction in OOP refers to the concept of hiding the complex implementation details
# and exposing only the necessary and relevant parts of an object or system.
# This helps in reducing complexity and increases efficiency.# Abstraction example in Python OOP
