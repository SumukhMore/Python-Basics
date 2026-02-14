# Create student database (dictionary)
student = {}

# Taking input
student["name"] = input("Enter student name: ")
student["roll_no"] = input("Enter roll number: ")
student["marks"] = float(input("Enter marks: "))

# Print details
print("\nStudent Details:")
print("Name:", student["name"])
print("Roll No:", student["roll_no"])
print("Marks:", student["marks"])

# Update marks
update = input("\nDo you want to update marks? (yes/no): ")

if update.lower() == "yes":
    new_marks = float(input("Enter new marks: "))
    student["marks"] = new_marks
    print("Marks updated successfully!")

# Check if key exists
key_check = input("\nEnter key to check (name/roll_no/marks): ")

if key_check in student:
    print("Key exists! Value:", student[key_check])
else:
    print("Key does not exist.")

# Final student data
print("\nFinal Student Data:", student)