# type conversion / type casting

# converting one data type to another data type is called type conversion or type casting

# two types of type conversion
# 1. implicit type conversion
# 2. explicit type conversion

# 1. implicit type conversion
# In this type of conversion, python automatically converts one data type to another data type.
# This process doesn't need any user involvement.

# 2 . explicit type conversion
# In this type of conversion, users convert the data type of an object to required data type.

# type conversion functions
# 1. int() - converts any data type to int
# 2. float() - converts any data type to float
# 3. str() - converts any data type to string
# 4. bool() - converts any data type to bool
# 5. complex() - converts any data type to complex
# 6. list() - converts any data type to list
# 7. tuple() - converts any data type to tuple
# 8. set() - converts any data type to set
# 9. dict() - converts any data type to dictionary
# 10. frozenset() - converts any data type to frozenset
# 11. bytes() - converts any data type to bytes
# 12. bytearray() - converts any data type to bytearray
# 13. memoryview() - converts any data type to memoryview


# example of explicit type conversion

# int to other data type
a = 10
print(a)
print(type(a))
f = float(a)
print(f)
print(type(f))
b = bool(a)
print(b)
print(type(b))
s = str(a)
print(s)
print(type(s))
c = complex(a) # 10+0j
print(c)
print(type(c))

# float to other data type
x = 5.5
print(x)
print(type(x))
i = int(x)
print(i)
print(type(i))
b = bool(x)
print(b)
print(type(b))
s = str(x)
print(s)
print(type(s))
c = complex(x) # 5.5+0j
print(c)
print(type(c))

# bool to other data type
b = True
print(b)
print(type(b))
i = int(b)
print(i)
print(type(i))
f = float(b)
print(f)
print(type(f))
s = str(b)
print(s)
print(type(s))
c = complex(b) # 1+0j
print(c)
print(type(c))

# str to other data type
s = "10"
print(s)
print(type(s))
i = int(s)
print(i)
print(type(i))
f = float(s)
print(f)
print(type(f))
b = bool(s) # True for any non-empty string
print(b)
print(type(b))
c = complex(s) # 10+0j
print(c)
print(type(c))


# complex to other data type
c = 5+3j
print(c)
print(type(c))
# i = int(c) # TypeError: can't convert complex to int
print(i)
print(type(i))
# f = float(c) # TypeError: can't convert complex to float
print(f)
print(type(f))
# b = bool(c) # TypeError: can't convert complex to bool
print(b)
print(type(b))
# s = str(c) # TypeError: can't convert complex to str
print(s)
print(type(s))

# None to other data type
n = None
print(n)
print(type(n))

# none can't be converted to any other data type except bool
b = bool(n) # False
print(b)
print(type(b))

# i = int(n) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
# print(i)
# print(type(i))
# f = float(n) # TypeError: float() argument must be a string or a number, not 'NoneType'



# list to other data type
lst = [10, 20, 30, 40]
print(lst)
print(type(lst))
t = tuple(lst)
print(t)
print(type(t))
s = set(lst)
print(s)
print(type(s))
d = dict(enumerate(lst))
print(d)
print(type(d))
fs = frozenset(lst)
print(fs)
print(type(fs))


# int to list
a = 10
print(a)
print(type(a))
lst = list(str(a))
print(lst)
print(type(lst))


