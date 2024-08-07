# Python Dictionary
# A dictionary is a collection of key-value pairs.

# A dictionary in Python is an unordered collection of items. Each item is a pair consisting of a key and a value.
# python dictionary is immutable, unordered, and keys to access values.

# Creating a Dictionary
# dictionary can be create using curly braces {} or the dict() function.
# example1 = {key1: value1, key2: value2, key3: value3}
# example2 = dict({key1: value1, key2: value2, key3: value3})

# Each key-value pair maps the key to its associated value.
# Keys must be unique in a dictionary, duplicate keys are not allowed.
# A key is an immutable data type such as a string, number, or tuple.
# A value can be any data type and can be duplicated.

dict1 = {'abacus': 'a counting tool', 'bachelor': 'Unmarried person', 'cable': 'A wire'}
print(dict1)

print(type(dict1))
print(len(dict1))

# Accessing Elements
# To access dictionary elements, you can use the square brackets along with the key to obtain its value.
# example: dict1[key]
print(dict1['abacus'])

# If the key is not found in the dictionary, a KeyError is raised.
# print(dict1['myKey'])  # KeyError: 'myKey'

