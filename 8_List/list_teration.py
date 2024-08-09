# Iterating a list
# Iterating /accessing / traversing a list means to access each element of the list one by one. 

# There are 3 ways to iterate a list:
# 1. Using for loop
# 2. Using while loop
# 3. Using for loop range() function

# Using for loop
list1 = [10, 12, 31, 14, 50]

for x in list1: # x is a variable that will store the value of each element of the list one by one
    print(x) # it will print the value of list in forward direction

# Output: 10 12 31 14 50 (next line)

# Using while loop
list2 = [10, 12, 31, 14, 50]

i = 0
while i < len(list2):
    print(list2[i])
    i += 1

# Output: 10 12 31 14 50 (next line)

# Using for loop range() function
list3 = [10, 12, 31, 14, 50]

for i in range(len(list3)):
    print(list3[i])

# Output: 10 12 31 14 50 (next line)
# Note: range() function generates a sequence of numbers starting from 0 to n-1 where n is the length of the list.

# -ve indexing

for i in range(len(list3)-1, -1, -1):
    print(list3[i],end=" ")
