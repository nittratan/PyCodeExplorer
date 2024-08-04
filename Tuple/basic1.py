# Iteration: traversing and visiting all the elements of a tuple .

t1= ('Jack', 45, 38.6, False, 5+6j,'Adam', 45) #this is a tuple

for i in t1:
    print(i)

for i in range(len(t1)):
    print(t1[i])

# Operators in tuple
# Index => []
# Slicing => [:]
# Concatenation => +
# Repeat => *
# Membership => in
# Membership => not in

# indexing
print(t1[0]) # Jack

t1[1]=80 # TypeError: 'tuple' object does not support item assignments

# slicing
print(t1[:]) # ('Jack', 45, 38.6, False, (5+6j), 'Adam', 45)
print(t1[0:3]) # ('Jack', 45, 38.6)
print(t1[2:5]) # (38.6, False, (5+6j))
print(t1[0:6:2]) # ('Jack', 38.6, (5+6j))
print(t1[-2::-1]) # ('Adam', (5+6j), False, 38.6, 45, 'Jack')

# concatenation 
# create another tuple 
t2 = ('John', 50, 48.6, True, 7+8j, 'Adam', 50)
t3 = t1+t2
print(t3) # ('Jack', 45, 38.6, False, (5+6j), 'Adam', 45, 'John', 50, 48.6, True, (7+8j), 'Adam', 50)

# repeat
t4 = t1*2
print(t4) # ('Jack', 45, 38.6, False, (5+6j), 'Adam', 45, 'Jack', 45, 38.6, False, (5+6j), 'Adam', 45)

# membership
print(45 in t1) # True
print(100 in t1) # False
print(100 not in t1) # True

if 45 in t1:
    print("45 is present in t1")

if 100 not in t1:
    print("100 is not present in t1")