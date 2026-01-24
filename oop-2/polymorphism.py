class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(self.real, "i+", self.imag, "j")
    
    def add(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)
    
num1 = Complex(2, 3)
num1.showNumber()

num2 = Complex(4, 5)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

"""
Operator & Dunder functions:
a + b --> a.__add__(b)
a - b --> a.__sub__(b)
a * b --> a.__mul__(b)
a / b --> a.__truediv__(b)
a // b --> a.__floordiv__(b)
a % b --> a.__mod__(b)
a ** b --> a.__pow__(b)
a == b --> a.__eq__(b)
a != b --> a.__ne__(b)
a > b --> a.__gt__(b)
a < b --> a.__lt__(b)
a >= b --> a.__ge__(b)
a <= b --> a.__le__(b)
"""