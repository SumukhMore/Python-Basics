# Create empty set to store emails
emails = set()

# Take 5 email inputs
for i in range(5):
    email = input(f"Enter email {i+1}: ")
    emails.add(email)

# Print unique emails
print("\nUnique Emails:")
for e in emails:
    print(e)