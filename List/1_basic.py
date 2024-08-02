# List is a collection of elements, or list is a collection of objects.

# list is mutable, that is, it can be changed after creation

# list is just like an array in other programming languages

"""
List is a collection of ordered objects and can have duplicates
It is created using [ ] and items inside are separated using a ( , ) comma
A list have +ve and -ve index as well
A list can be created in 2 ways that is
List1 = [ 1,2,3,4,5 ]
List2 = list( ( 1,2,3,4,5 ) )

"""

lst1 = [1, 2, 3, 4, 5]
lst2 = list((1, 2, 3, 4, 5))
lst3 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# List is heterogeneous means a list allows different type of data. It can have string, integer, float, etc.

lst4 =['item' , 7 , 'price' , 9.99]

print(lst1)
print(lst2)

# Accessing the list elements
print(lst1[0])  # 1
print(lst1[1])  # 2

# Accessing the list elements using -ve index
print(lst1[-1])  # 5
print(lst1[-2])  # 4

lst1[0] = 10
print(lst1)  # [10, 2, 3, 4, 5]

lst1.append(6)

print(type(lst1))  # <class 'list'>

print(dir(lst1))