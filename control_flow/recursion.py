#print numbers from n to 1 using recursion
def show (n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)

#factorial of a number using recursion
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))