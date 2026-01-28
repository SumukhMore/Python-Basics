# WAP to check if a number entered by the user is odd or even.

num = int(input("Enter an integer number: "))

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")