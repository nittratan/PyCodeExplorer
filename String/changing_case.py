# string in python are immutable, so we can't change the case of a string directly. 
# But we can convert the string to upper case or lower case using some built-in methods.
# It creates a new string with the changed case and returns it.


# string case conversion/ changing case

# upper() method
# lower() method
# title() method
# capitalize() method
# swapcase() method
# casefold() method

str = "Hello, Everyone!"

# upper() method
print(str.upper()) # convert all characters in the string to uppercase

# lower() method
print(str.lower()) # convert all characters in the string

# title() method
print(str.title()) # Capitalize the first letter of each word

# capitalize() method
print(str.capitalize()) # Capitalize the first letter of the string

# swapcase() method
print(str.swapcase()) # swap the case of each character in the string

# casefold() method
print(str.casefold()) # convert the string to lowercase and remove all case distinctions


str1 = "Hello, 123"
str2 = "hello, 123"

print(str1.upper())
print(str2.upper())

