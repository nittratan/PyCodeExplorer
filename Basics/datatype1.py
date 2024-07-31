# datatype in Python

# numeric data type in python
# numeric data type in python supports single value , just one value at a time

# 1. int
# 2. float
# 3. bool
# 4. complex


# ------------------------------------------------------------------------------------------


# sequence data type in python
# the sequence data type holds the collection of values. Values can be of any data type
# 1. str
# 2. list # mutable :  means we can change the values
# 3. tuple # immutable : means we can't change the values
# bytes
# bytearray
# range

# in sequence data type, we can access the values by using index number


# ------------------------------------------------------------------------------------------


# set data type in python
# set data type in python holds the collection of values but it does not support duplicate values
# there is no index number in set data type
# 1. set # mutable : means we can change the values
# 2. frozenset # immutable : means we can't change the values


# ------------------------------------------------------------------------------------------

# mapping data / Dictionary type in python
# dictionary data type in python holds the collection of key-value pairs
# key must be unique and immutable
# value can be of any data type
# it is useful to storing the data and retriving/ accessing the data much faster
# 1. dict 
# mutable : means we can change the values

# ---------------------------------------Examples---------------------------------------------------
# int
a = 50
print(a)

# float
x = 5.5
print(x)
print(type(x))

# complex
c = 5+3j
print(c)
print(type(c))
print(c.real)
print(c.imag)

# bool
b = True
print(b)
print(type(b))
print(5+True)
print(int(True))

# str
s = "Hello World"
print(s)
print(type(s))

# None
n = None
print(n)
print(type(n))

# bytes
bt = b"Hello"
print(bt)
print(type(bt))
# ------------------------------------------------------------------------------------------

# sequence data type in python
# str
s = "Hello World"
print(s)
print(type(s))

# list
lst = [10, 20, 30, 40]
print(lst)
print(lst[2])
print(type(lst))

# tuple
t = (10, 20, 30, 40)
print(t)
print(t[2])
print(type(t))

# bytes
bt = b"Hello"
print(bt)
print(type(bt))

# bytearray
bt = bytearray(b"Hello")
print(bt)
print(type(bt))

# range
r = range(10)
print(r)
print(type(r))

# ------------------------------------------------------------------------------------------
# set data type in python
# set
s = {10, 20, 30, 40}
print(s)

# frozenset
fs = frozenset({10, 20, 30, 40})
print(fs)


# ------------------------------------------------------------------------------------------
# mapping data / Dictionary type in python
# dict
dct = {111:'Ratan', 222:'Suraj'}
print(dct)
print(dct[111])
print(type(dct))

