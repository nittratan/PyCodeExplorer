# packing and unpacking

# packing
t1 =10
print(t1)
print(type(t1))

t1 = 10, 20, 30 , 40 , 50 # packing

"""

if multiple values just separated by comma, it will pack them in a tuple. 
It will pack them. So this is called as packing.

"""
print(t1)
print(type(t1)) # <class 'tuple'>


# unpacking
a , b ,c , d , e = t1 # unpacking
print(a)
print(b)
print(c)
print(d)
print(e)

# unpacking supports with any iterable like list, set, dictionary, etc. but packing is only supported with tuple

# unpacking with list
lst = [10, 20, 30, 40, 50]
a, b, c, d, e = lst
print(a)
print(b)
print(c)
print(d)
print(e)

t2  = (10, 20, 30, 40, 50)
a ,b , c = t2 # ValueError: not enough values to unpack (expected 3, got 5)

