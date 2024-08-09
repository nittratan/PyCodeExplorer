# Dictionary comprehensions provide a concise way to create dictionaries in Python. 
# They are similar to list comprehensions but produce dictionary objects.

# Dictionary comprehensions are a way to build a new dictionary by applying an expression to each item in an iterable.

# Syntax
# {key: value for item in iterable if condition}
'''
    key: Expression for the key.
    value: Expression for the value.
    iterable: A collection of items to iterate over.
    condition (optional): A conditional expression to filter items.

'''

dict1 = {} # empty dictionary 
print(type(dict1))
dict2 = dict() # empty dictionary
print(type(dict2))

dict2["apple"] = "A fruit"
dict2["ball"] = "A round object"
dict2["patna"] = "Capital of Bihar"

for i in range(1, 6):
    dict2[i] = 2*i

print(dict2)

# Dictionary Comprehensions
# syntax 
# dict3 = dict[pair of iterable]

dict3 = dict(((1,2), (2,4), (3,6), (4,8), (5,10))) # dictionary comprehension using tuple
print(dict3)
print(type(dict3))

dict4 = dict([["apple", "A fruit"], ["ball", "A round object"], ["patna", "Capital of Bihar"]]) # dictionary comprehension using list
print(dict4)

l1 = ["apple", "ball", "patna"]
l2 = ["red", "round", "Bihar"]
dict5 = dict(zip(l1, l2)) # dictionary comprehension using zip function | zip function is used to combine two lists
print(dict5)


# enumerate() function
# enumerate() function adds a counter to an iterable and returns it in a form of enumerate object.
List1 = ["apple", "ball", "patna"]
for item in enumerate(List1): # enumerate function will return a tuple of index and value
    print(item) 

# enumerating means giving numbers numbering to the items in the iterable.

# Dictionary Comprehensions
dict6 = dict(enumerate(List1)) # dictionary comprehension using enumerate function
print(dict6)

# Dictionary Comprehensions
dict7 = {i: i**2 for i in range(1, 6)} # dictionary comprehension using for loop
print(dict7)

dict8 = dict((i , i*3) for i in range(1, 6)) # dictionary comprehension using for loop
print(dict8)

dict9 = {i: i**2 for i in range(1, 11) if i%2 == 0} # dictionary comprehension using for loop and condition
print(dict9)