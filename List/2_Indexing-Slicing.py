# List: Indexing and Slicing

# Indexing
# Indexing is used to access the elements of a list. Indexing can be done in two ways:
# Positive Indexing
# Negative Indexing

# Slicing
# slice = lst[start:stop:step]
# start: starting index of the slice
# stop: ending index of the slice
# step: step size of the slice

# list operators
# + Concatenation operator
# * Repeat operator
# in Membership operator
# not in Membership operator
# [] index operator
# [:] slice operator
# [: :] slice operator

# Indexing

lst = [10,15,20,25,30,35,40,45,50]

# Positive Indexing
print(lst[0])  # 10
print(lst[1])  # 15

# Negative Indexing
print(lst[-1])  # 50
print(lst[-2])  # 45

# Slicing
# slice = lst[start:stop:step]
print(lst[:]) # [10, 15, 20, 25, 30, 35, 40, 45, 50]
print(lst[0:3])  # [10, 15, 20]
print(lst[2:5])  # [20, 25, 30]
print(lst[0:6:2])  # [10, 20, 30]
print(lst[-2::-1])  # [45, 40, 35, 30, 25, 20, 15, 10]

x = lst[-2]
print(x)  # 45

lst[-2] = 100
lst[1]= 200
print(lst)  # [10, 200, 20, 25, 30, 35, 40, 100, 50]

# membership operator
print(20 in lst)  # True
print(200 in lst)  # False
print(200 not in lst)  # True

if 20 in lst:
    print("20 is present in lst")

if 200 not in lst:
    print("200 is not present in lst")