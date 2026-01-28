# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movies = []
mov1 = input("Enter the name of your first favorite movie: ")
mov2 = input("Enter the name of your second favorite movie: ")
mov3 = input("Enter the name of your third favorite movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print("Your favorite movies are:", movies)