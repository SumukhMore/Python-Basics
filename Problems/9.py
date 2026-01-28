# WAP to check if a  number is a multiple of 7 or not.

x = int(input("Enter an integer number: "))
if x % 7 == 0:
    print(x, "is a multiple of 7.")
else:
    print(x, "is not a multiple of 7.")