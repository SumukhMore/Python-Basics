i = 1
while i <= 10:
    print(i)
    i += 1
print("Loop ended.") # This code prints numbers from 1 to 10 using a while loop and then indicates that the loop has ended.

i = 10
while i >= 1:
    print(i)
    i -= 1
print("Countdown finished.") # This code counts down from 10 to 1 using a while loop and then indicates that the countdown is finished.

i = 1
while i <= 20:
    print(i)
    i -= 1
print("This will run forever unless stopped.") # This code attempts to print numbers starting from 1 and decrementing, which will lead to an infinite loop.

#Break Statement
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at idx", i)
        break
    else:
        print("finding...")
    i += 1

print("End of loop.") # This code searches for the number 36 in a list of perfect squares using a while loop and breaks out of the loop when found.


#Continue Statement
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1