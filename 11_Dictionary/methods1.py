# Looping over Dictionary

# Looping over a dictionary using for loop

myDict = {101:"Production", 102:"Marketing", 103:"Sales", 104:"Finance", 105:"HR", 106:"IT"}

for key in myDict: # by default it will iterate over the keys of the dictionary
    print(key)

for key in myDict: # by default it will iterate over the keys of the dictionary
    print(key, myDict[key]) # to print the key value pair [] is used to access the value of the key


# using get() method
# get() method is used to access the value of the key
# Syntax:
# value = dictionary.get(key, default_value)
# key: The key to search for in the dictionary.
# default_value (optional): The value to return if the key is not found. The default is None.

for key in myDict:
    print(key, myDict.get(key))

myDict.get(101) # to access the value of the key

print(myDict.get(107, "Hello Your key is not found") )# if the key is not present in the dictionary then it will return None

print(myDict.get(101 , None) ) # if the key is present in the dictionary then it will return the value of the key otherwise it will return None

# myDict[107] # if the key is not present in the dictionary then it will throw an error
# myDict.get(107) # if the key is not present in the dictionary then it will return None


# keys() method
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
student = {"roll":101, "name": "Sheetal", "age": 25, "grade": "A"}
print(student.keys())
print(type(student.keys())) # it will return a view object

for key in student.keys():
    print(key)

# values() method
# The values() method returns a view object that displays a list of all the values in the dictionary.
print(student.values())
print(type(student.values())) # it will return a view object

for value in student.values():
    print(value)


# items() method
# The items() method returns a view object that displays a list of dictionary's key-value tuple pairs.

print(student.items())
print(type(student.items())) # it will return a view object

for item in student.items():
    print(item)

for key, value in student.items():
    print(key, value)