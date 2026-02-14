num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Handle division by zero
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Error! Division by zero is not allowed.")