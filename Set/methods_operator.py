# set methods and operators

# methods
# add()
# copy()
# update()

# pop()
# remove()
# discard()
# clear()

# operators
# membership operators
# in
# not in


# add() method is used to add elements in the set
s = {10,20,30,40,50}
print(len(s)) # 5
s.add(60)
print(s) 
print(len(s)) # 6


# copy() method is used to copy the elements of the set to another set
s1 = s.copy()
print(s1) # {50, 20, 40, 10, 60, 30}


# update() method is used to add elements of one set to another set
s2 = {70,80,90}
s.update(s2)
print(s) 
s2.update((11,22))
print(s2)
s2.update([33,44])
print(s2)
s2.update('Python')

print(s2) 


# pop() method is used to remove and return an arbitrary element from the set
s3 = {10,20,30,40,50}
print(s3.pop()) # it can remove any element from the set


# remove() method is used to remove the specified element from the set if element is not present it will throw an error
s3.remove(20)
print(s3)
# s3.remove(20) # KeyError: 20


# discard() method is used to remove the specified element from the set if element is not present it will not throw an error
s3.discard(30)
print(s3)
s3.discard(30) # no error


# clear() method is used to remove all the elements from the set
s3.clear()
print(s3) # set()


# membership operators : in & not in
s4 = {10,20,30,40,50}
print(10 in s4) # True
print(60 in s4) # False

print(10 not in s4) # False
print(60 not in s4) # True

if 10 in s4:
    print('10 is present in the set')
else:
    print('10 is not present in the set')
