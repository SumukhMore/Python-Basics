filename = "diary.txt"

while True:
    print("\n--- Diary Menu ---")
    print("1. Write New Entry")
    print("2. Read Diary")
    print("3. Exit")

    choice = input("Choose (1-3): ")

    if choice == "1":
        entry = input("Write your diary message:\n")

        with open(filename, "a") as file:
            file.write(entry + "\n")
            file.write("-" * 30 + "\n")

        print("Entry saved successfully!")

    elif choice == "2":
        print("\n--- Your Diary ---")

        try:
            with open(filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No diary found. Write first entry!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
