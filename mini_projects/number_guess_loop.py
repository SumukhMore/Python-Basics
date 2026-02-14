secret_number = 7

# Start the guessing loop
while True:
    guess = int(input("Enter your guess:"))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    else:
        print("Try again!")