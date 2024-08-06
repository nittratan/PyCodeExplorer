# Comprehensions: - It's a simple and easy way of creating sets from other iterables.

s = set()
for x in range(1,6):
    s.add(x)

print(s) # {1, 2, 3, 4, 5} order may be different

# Syntax: {expression for item in iterable}
s1 = set() # empty set
s1.add(10)
s1.add(20)

print(s1) # {10, 20}

# set comprehension
s2 = {x*x for x in range(1,6)}
print(s2) # {1, 4, 9, 16, 25}

# set comprehension with if condition
s3 = {x*x for x in range(1,11) if x%2 == 0}
print(s3) # {64, 100, 4, 36, 16}

# set comprehension with if else condition
s4 = {x*x if x%2 == 0 else x*x*x for x in range(1,11)}
print(s4) 

s5 = {x.upper() for x in 'python'}
print(s5) 

s6 = {1,23 , 'Hello' ,{1,2,3},[1,2,3]} # TypeError: unhashable type: 'set'
# set contains only hashable elements like int, float, string, tuple etc. 
# it can't contain mutable elements like list, set, dictionary etc.