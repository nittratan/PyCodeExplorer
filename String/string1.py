# operators on string

# concatenation
# repetition
# slicing
# indexing
# in 
# not in

# concetenation of string : + operator
# concatenation of string means joining two or more strings to form a new string.

# Example:
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print(s3)

# s3 = "hello" + 15 # not allowed 
# s3 = "hello" + str(15) # allowed

s4 = "hello" + "how" + "are" + "you"
print(s4)



# repetition of string : * operator
# repetition of string means repeating the same string multiple times.

# Example:
s5 = "hello" * 3 # only integer is allowed
print(s5) # hellohellohello



# indexing of string
# Indexing of string means accessing the elements of string using index.

# Example:
s6 = "Hello World"
# index starts from 0 to n-1 where n is the length of string.
# H -> 0 e -> 1 l -> 2 l -> 3 o -> 4 W -> 5 o -> 6 r -> 7 l -> 8 d -> 9

# negative indexing
# H -> -10 e -> -9 l -> -8 l -> -7 o -> -6 W -> -5 o -> -4 r -> -3 l -> -2 d -> -1


print(s6[0]) # H
print(s6[-1]) # d

for x in s6:
    print(x,end=' ')

for i in range(len(s6)):
    print(s6[i],end=' ')

print("\n") # new line

# print in reversed order
for i in range(len(s6)-1,-1,-1):
    print(s6[i],end=' ')


# slicing of string
# Slicing of string means extracting a substring from the given string.


# syntax: string[start:end:step]

# Example:
s7 = "Hello World"
print(s7[0:5]) # Hello
print(s7[6:11]) # World
print(s7[:5]) # Hello
print(s7[6:]) # World
print(s7[:]) # Hello World
print(s7[::2]) # HloWrd
print(s7[::-1]) # dlroW olleH
print(s7[5:0:-1] )# olleH

print(s7[4:8:1]) # o W

str = "welcome"
print(str[2:5:1]) # lco


# in / not in operator
# in operator is used to check whether a substring is present in the given string or not.
# boolean value will be returned.


# Example:
s8 = "Hello World"
print("Hello" in s8) # True
print("Hello" not in s8) # False
print("World" in s8) # True
print("World" not in s8) # False

