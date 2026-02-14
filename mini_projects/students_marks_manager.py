# Store marks of 5 students
marks = []

# Take marks input
for i in range(5):
    score = float(input(f"Enter marks of student {i+1}: "))
    marks.append(score)

# Print all marks
print("\nAll Student Marks:", marks)

# Calculate total and average
total_marks = sum(marks)
average_marks = total_marks / len(marks)

# Print results
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)