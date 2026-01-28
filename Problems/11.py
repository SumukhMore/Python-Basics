# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("list1 contains a palindrome.")
else:
    print("list1 does not contain a palindrome.")