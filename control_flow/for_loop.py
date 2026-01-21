#for loop in Python
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in num:
    print(i)
print("Loop ended.") # This code prints numbers from 1 to 10 using a for loop and then indicates that the loop has ended.

str = "Sumukh"
for char in str:
    print(char)
print("String loop ended.") # This code prints each character in the string "Sumukh" using a for loop and then indicates that the string loop has ended.

tuple_nums = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
for n in tuple_nums:
    if n % 4 == 0:
        print(n)
print("Even numbers loop ended.") # This code prints even numbers from a tuple that are divisible by 4 using a for loop and then indicates that the even numbers loop has ended.

#for loop with else

str = "Python"
for char in str:
    if char == 'h':
        print("Found h!")
        break
    print(char)
else:
    print("END") # This code searches for the character 'h' in the string "Python" using a for loop and breaks out of the loop when found; if not found, it prints "END".

#Range Function
for i in range(10): #stop
    print(i)

for i in range(5, 15): #start, stop
    print(i)

for i in range(1, 20, 2): #start, stop, step
    print(i) # This code demonstrates the use of the range function in for loops to print numbers in different ranges and steps.