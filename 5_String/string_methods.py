# string methods
# Python provides many built-in methods to manipulate strings. Some of the important string methods are:

# len() : returns the length of string.
# find() : returns the index of first occurrence of substring.
# rfind() : returns the index of last occurrence of substring.
# index() : returns the index of first occurrence of substring.

str = "Hello, How are you?"

print(len(str)) # 18

# find() method
# syntax: str.find(substring)

print(str.find("How")) # 7
print(str.find("how")) # -1 (not found)
print(str.rfind("o")) # 15

#rfind() method
# syntax: str.rfind(substring)
# rfind() method returns the index of last occurrence of substring. search starts from right to left.
print(str.rfind("o")) # 15


# index() method
# syntax: str.index(substring)
# index() method returns the index of first occurrence of substring. If substring is not found then it raises ValueError.
print(str.index("How")) # 7
# print(str.index("how")) # ValueError: substring not found

# count() method
# syntax: str.count(substring)
# count() method returns the number of occurrences of substring in the given string.
print(str.count("o")) # 3
print(str.count("z")) # 0

# replace() method
# syntax: str.replace(old,new)
# replace() method replaces all occurrences of old substring with new substring.
print(str.replace("How","Where")) # Hello, Where are you?

# remove whitespaces using replace() method
str = " Hello, How are you? "
print(str.replace(" ","")) # Hello,Howareyou?
print(str.replace(" ","@") )# Hello,@How@are@you?

# string alignment using ljust(), rjust() and center() methods
str = "  Hello  "
print(str.ljust(10,"*")) # Hello*****
print(str.rjust(10,"*")) # *****Hello
print(str.center(10,"*")) # **Hello***

# strip() method
# syntax: str.strip()
# strip() method removes whitespaces from both ends of the string.
str = "  Hello  "
print(str.strip()) # Hello

str1  = "    Python    "
print(str1.strip()) # Python
print(str1.lstrip()) # Python
print(str1.rstrip()) #     Python

str1 = "&.Hello, How are you?."
print(str1.strip("&.")) # Hello, How are you?
