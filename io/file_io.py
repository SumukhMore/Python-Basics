f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

# import os
# os.remove("sample.txt")  # to remove a file

# r = read
# w = write
# a = append
# r+ = read and write
# w+ = write and read
# a+ = append and read
# b = binary mode
# t = text mode
# + = update
# x = create
