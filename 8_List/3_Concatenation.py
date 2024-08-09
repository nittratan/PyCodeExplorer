# Concatenation of lists
# Concatenation is the process of joining two or more lists together to create a new list.

list1 = [1,2,3]
list2 = [8,9,10]

# + operator is used to concatenate two lists

list3 = list1+list2 # concatenation of list1 and list2. list1 and list2 are not changed
print(list3)

# newLst= list1+4 # not allowed , only list can be concatenated with list

newlist = list1+[4] # allowed 
print(newlist)

list1.extend([6,7,9]) # extend the list1

print(list1)

list2 = list2+[5,8,11] 
print(list2)

# * operator is used to repeat the list elements
newLst = list1*2
print(newLst)

# in operator is used to check if an element is present in the list or not
print(4 in list1) # True

if 4 in list1:
    print("4 is present in list1")
else:
    print("4 is not present in list1")

# not in operator is used to check if an element is not present in the list or not
print(4 not in list1) # False

if 4 not in list1:
    print("4 is not present in list1")
else:
    print("4 is present in list1")