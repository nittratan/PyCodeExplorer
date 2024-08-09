'''

It is a method to create a list in a simple way from existing list (or) other iterables.
A list can be generated from a list , tuple , string or a set.
A list can be empty, it is denoted as [ ]
append( ) in list adds an element to a list
A loop can be used to append values in a list of particular range.

'''

# List Comprehensions : comprehensions are short cut for creating a sequence object or list object.

lst = []
for x in range(10):
    lst.append(x)

print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l1 = [x for x in range(10)]
print(l1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l2 = [x for x in range(10) if x%2==0]
print(l2) # [0, 2, 4, 6, 8]

l3 = [x**2 for x in range(10)]
print(l3) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

l4 = [x.lower() for x in 'Python']
print(l4) # ['p', 'y', 't', 'h', 'o', 'n']

l5 = [x for x in "ab12@cd-sheu@#*" if x.isalpha()]  
print(l5) # ['a', 'b', 'c', 'd', 's', 'h', 'e', 'u']