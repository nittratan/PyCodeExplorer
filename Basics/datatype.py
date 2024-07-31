# data type in python
# 1. int

a = 50
print(a)
print(type(a))

# 2. float
x = 5.5
print(x)
print(type(x))

# size of int and float
import sys
print(sys.getsizeof(a))
print(a.__sizeof__())   # another way to get size of int

# there is no limit of int in python and its size is depend on the memory of system

# there is not fixed size of memory taken by any data type in python. That's is the reason that allow bigger number in python

# 3. complex
c = 5+3j
print(c)
print(type(c))
print(c.real)
print(c.imag)

# 4. bool
b = True
print(b)
print(type(b)) # bool is a subclass of int
print(5+True) # 5+1 = 6
print(int(True)) # 1

# 5. str
s = "Hello World"
print(s)
print(type(s))

# 6. None
n = None
print(n)
print(type(n))
# non is a singleton object in python
# it can't be converted to any other data type except bool (Type casting)

# 7. bytes
bt = b"Hello"
print(bt)
print(type(bt))
