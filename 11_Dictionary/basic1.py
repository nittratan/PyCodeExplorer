# Python Dictionary

# How to access , insert , modify/update and delete elements in a dictionary
# to access , insert , modify/update and delete elements in a dictionary we use the key of the element.
# key must be present in the dictionary otherwise it will raise an error.

dic1 = {101:"Raju", 102:"Ravi", 103:"Rahul", 104:"Raman", 105:"Rohit"}

# Accessing Elements
# To access dictionary elements, you can use the square brackets along with the key to obtain its value.
print(dic1[103])  # Rahul
print(dic1[105])  # Rohit
# print(dic1[1])  # Error: KeyError: 1 # Key is not found in the dictionary so it will raise an error 
# give only that key which is present in the dictionary

# Modifying/Updating Elements
# To modify the value of a specific item, refer to its key name.
dic1[103] = "Rahul Kumar"
print(dic1[103])  # Rahul Kumar
print(dic1)

# Inserting Elements
# To insert a new item in the dictionary, you can assign a new value to a new key.
dic1[106] = "Ramesh Kumar"
print(dic1[106])  # Ramesh Kumar
print(dic1)

# Deleting Elements 
# You can remove a particular item in a dictionary by using del.
del(dic1[106])
print(dic1)

# traverse the dictionary
# we can traverse the dictionary using for loop
for key in dic1: # default it will print only keys
    print(key) # it will print all the keys of the dictionary

for key in dic1:
    print(key , dic1[key]) # it will print all the keys and values of the dictionary

for key , value in dic1.items():
    print(key , value) # it will print all the keys and values of the dictionary


# insert using for loop
dic2 = {}
for i in range(1, 6):
    dic2[i] = i*i
print(dic2)

# insert using for loop user input
dic3 = {}
n = int(input("Enter the number of elements: "))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dic3[key] = value
print(dic3)
