# Tuple : Immutable list of items that are ordered and indexed
# can not be changed, modified or manipulated
# can be created using ()
# Tuple is faster than list
# Tuple is used when data is fixed
# tuple can contain different data types
# duplicate items are allowed

# --------------------------------------------------------------------------------
# List Vs Tuple
# list is mutable, tuple is immutable
# lst = [], tup = ()  or lst = list(), tup = tuple()
# list is slower than tuple
# list is used when data is dynamic
# tuple is used when data is fixed
# both can contain different data types
# both can contain duplicate items
# tup = (1, 2, 3, 4, 5)
# tup[0] = 10 # not allowed
# tup.append(6) # not allowed

# --------------------------------------------------------------------------------
# tupple can be created in different ways
# 1. tpl = (1 , 2, 3, 4, 5)
# 2. tpl = tuple((1, 2, 3, 4, 5)) # any iterable can be converted to tuple using tuple function it accepts only one argument
# 3. tpl = () # empty tuple
# 4. tpl = (1,) # tuple with single item
# 5. tpl = (1) # not allwoed, it will be considered as int

tuple1=('Jack', 45,38.6,False, 5+6j, 'Adam', 45)
print(tuple1)
print(type(tuple1)) 
print(tuple1[0])
print(tuple1[1])

# tuple1[0] = 'John' # not allowed as tuple is immutable Error not support assignment

tuple2 = (12) # not allowed, it will be considered as int
print(tuple2)
print(type(tuple2))

tuple3 = (12,) # tuple with single item
print(tuple3)
print(type(tuple3))

tuple4 = tuple((1, 2, 3, 4, 5)) 
print(tuple4)
print(type(tuple4))

tuple5 = tuple([1, 2, 3, 4, 5]) # list to tuple conversion
print(tuple5)
print(type(tuple5))