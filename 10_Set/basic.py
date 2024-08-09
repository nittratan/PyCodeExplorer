# Python Set

'''
set is also collection of elements but it is unordered and unindexed and it does not allow duplicate elements.

In methematics
set is a collection of distinct elements.
ex A = {1,2,3,4,5}

'''

# => Set is also a collection of objects or collection of elements.
# => It's having a string type of value integer type of value, float type of value and string and a boolean type of value.
# => Iterable like list, tuple, dictionary, set, string, range, etc.
# => It is unordered and unindexed.
# => It does not allow duplicate elements.
# => It is mutable. We can add or remove elements from the set.
# => It is represented by {} curly braces.
# => elements can't be modified 
# => elements can be added or removed from the set

# how to create set in python
s1 = {'Jack', 45, 38.6, False, 5+6j, 'Adam', 45} # only distinct elements are allowed in the set 45 is present only once when printed
print(s1) # {False, 38.6, 45, 'Adam', 'Jack', (5+6j)} no duplicate elements allowed so 45 is present only once in the set
print(type(s1)) # <class 'set'>

# s2 = set(1,2,3,4,5) # TypeError: set expected at most 1 argument, got 5. Only one iterable argument is allowed
s2 = set([1,2,3,4,5]) # list to set conversion
print(s2) 

s3 = set((1,2,3,4,5)) # tuple to set conversion
print(s3) 

s4 = set('Python') # string to set conversion
print(s4) # {'P', 'h', 'o', 'n', 't', 'y'} # order cab be different

s5 = {10,20,30,40,50}  # ================= order is not preserved in set =====================
print(s5) # {50, 20, 40, 10, 30} # order cab be different 



# Accessing elements in set
# => We can not access elements in set using index because set is unordered and unindexed.
# print(s1[0]) # TypeError: 'set' object is not subscriptable (subscriptable means indexable)

s5.add(60) # add() method is used to add elements in the set
print(s5) # {50, 20, 40, 10, 60, 30}
print(len(s5)) # 6

s5.remove(60) # remove() method is used to remove elements from the set if element is not present it will throw an error
s5.discard(60) # discard() method is used to remove elements from the set if element is not present it will not throw an error
print(s5) # {50, 20, 40, 10, 30}

for s in s5:
    print(s , end=' ') # 50 20 40 10 30

for i in range(len(s5)): # TypeError: object of type 'set' has no index 
    print(s5[i])

