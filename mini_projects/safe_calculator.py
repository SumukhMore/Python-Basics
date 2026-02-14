while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2
        print("Result:", result)

        break   # exit loop if successful

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Please enter valid numbers only!")

    except Exception as e:
        print("Unexpected error:", e)

    print("Try again...\n")