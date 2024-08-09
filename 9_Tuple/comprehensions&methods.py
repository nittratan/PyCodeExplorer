# Comprehension: comprehensions are short cut for creating a sequence object or tuple object.

# Tuple Comprehensions : comprehensions are short cut for creating a sequence object or tuple object.

l1 = [x for x in range(10)] # list comprehension

t1 = (x for x in range(10)) # tuple comprehension : generator object
print(t1) # <generator object <genexpr> at 0x0000020E2B1C3E48>
# this will not create a tuple, it will create a generator object which is iterable

t2 = tuple(x for x in range(10)) # tuple comprehension 
print(t2) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

t3 = (*(x for x in range(10)),) # tuple comprehension
print(t3) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# methods : tuple has only two methods
# count() : returns the number of times a specified value occurs in a tuple
# index() : returns the index of the first occurrence of the specified value

tpl = (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
print(tpl.count(10)) # 2
print(tpl.index(10)) # 0
print(tpl.index(10, 1)) # 5

print(tpl.index(100)) # ValueError: tuple.index(x): x not in tuple