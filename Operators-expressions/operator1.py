# Arithmatic operators
a = 10
b = 20
print(a + b) # 30
print(a - b) # -10
print(a * b) # 200
print(a / b) # 0.5 (float division)
print(a // b) # 0 (integer division)
print(a % b) # 10 (remainder)
print(a ** b) # 100000000000000000000 (exponentiation)

# Comparison operators
print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

# Logical operators
a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False
print(not b) # True

# Bitwise operators
a = 10 # 1010
b = 20 # 10100
print(a & b) # 0 (bitwise AND)
print(a | b) # 30 (bitwise OR)
print(a ^ b) # 30 (bitwise XOR)
print(~a) # -11 (bitwise NOT)
print(a << 2) # 40 (left shift)
print(a >> 2) # 2 (right shift)

# Assignment operators
a = 10
a += 20
print(a) # 30
a -= 10
print(a) # 20
a *= 2
print(a) # 40
a /= 2
print(a) # 20.0
a //= 3
print(a) # 6.0

# Identity operators
a = 10
b = 10
print(a is b) # True
print(a is not b) # False
print(id(a))
print(id(b))
a = 10.5
b = 10.5
print(a is b) # False
print(a is not b) # True
print(id(a))
print(id(b))


# Membership operators
a = [10, 20, 30]
print(10 in a) # True
print(20 not in a) # False
print(40 in a) # False

# Ternary operator
a = 10
b = 20
print(a if a > b else b) # 20
