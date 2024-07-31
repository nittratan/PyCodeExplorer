# string inquires methods

# these methods are used to check the content of a string and return a boolean value.
# It returns True if the string meets the condition, otherwise False. => boolean value


# islower() method
# isupper() method
# istitle() method
# isdigit() method
# isalpha() method
# isspace() method
# isalnum() method
# isdecimal() method
# isnumeric() method
# isidentifier() method
# isprintable() method
# startswith() method
# endswith() method

str1 = "hello, everyone!"
str2 = "HELLO, EVERYONE!"
str3 = "Hello, Everyone!"
# islower() method
# The islower() method returns True if all the characters in the string are in lowercase, otherwise False.

print(str1.islower()) # True
print(str2.islower()) # False

if str1.islower():
    print("All characters in the string are in lowercase.")
else:
    print("All characters in the string are not in lowercase.")

# isupper() method
# The isupper() method returns True if all the characters in the string are in uppercase, otherwise False.
print(str1.isupper()) # False
print(str2.isupper()) # False

# istitle() method
print(str1.istitle()) # False
print(str2.istitle()) # False
print(str3.istitle()) # True

# isdigit() method : check string containing only digits
str = "12345"
print(str.isdigit()) # True

# isalpha() method : check string containing only alphabets
str = "Python"
print(str.isalpha()) # True

# isspace() method : check string containing only whitespaces
str = " "
print(str.isspace()) # True

# isalnum() method : check string containing only alphabets and digits
str = "Python123"
print(str.isalnum()) # True

# isdecimal() method : check string containing only decimal characters
str = "12345"
print(str.isdecimal()) # True

# isnumeric() method : check string containing only numeric characters
str = "12345"
print(str.isnumeric()) # True

# isidentifier() method : check string is a valid identifier or not
str = "Python"
print(str.isidentifier()) # True

# isprintable() method : check string is printable or not
str = "Hello, Everyone!"
str1 = "Hello, \nEveryone!"
print(str.isprintable()) # True
print(str1.isprintable()) # False (contains newline character) 
# \n is a newline character. It is not printable. So, it returns False.

# startswith() method : check string starts with a specific substring
str = "Hello, Everyone!"
print(str.startswith("Hello")) # True

# endswith() method : check string ends with a specific substring
str = "Hello, Everyone!"
print(str.endswith("Everyone!")) # True
print(str.endswith("Hello")) # False

# Note: These methods are used to check the content of a string and return a boolean value. It returns True if the string meets the condition, otherwise False.



