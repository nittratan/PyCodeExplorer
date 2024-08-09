# string join and split methods

# replace()
# join()
# split()
# rsplit()
# splitlines()

# replace() method
# syntax: str.replace(old,new , [,count]) count is optional
# replace() method replaces all occurrences of old substring with new substring. 
# If count is given, only first count occurrences are replaced.

str = "a-b-c-d-e-f"
str1 = str.replace("-","@")
str2 = str.replace("-","@",2)
print(str1) # a@b@c@d@e@f
print(str2) # a@b@c-d-e-f

email = "sratan@gmail.com"
new_email = email.replace("gmail.com","nitt.edu")
print(new_email) # sratan@nitt.edu

email ="sratan338@gmail.com"
print(email.replace("gmail","yahoo")) # sratan338@yahoo.com


# join() method
# syntax: str.join(iterable)
s1 = "Hello"
s2 = "Python"
newstring = s1.join(s2)
print(newstring) # PHelloyHellotHellohHellooHellon

lst = ["ajay","vijay","sujay"]
newstring = ",".join(lst)
print(newstring) # ajay,vijay,sujay
print(" ".join(lst)) # ajay vijay sujay
print("".join(lst)) # ajayvijaysujay

# split() method
# syntax: str.split(separator, maxsplit) maxsplit is optional
# split() method splits the string into a list of substrings.
# If separator is not provided, then it splits the string using whitespaces.
# If maxsplit is given, then it splits the string into at most maxsplit+1 parts.

str = "Hello, How are you?"
print(str.split()) # ['Hello,', 'How', 'are', 'you?'] # form a list of substrings using whitespaces

# splitlines() method
# syntax: str.splitlines(keepends)
# splitlines() method splits the string at line breaks and returns a list of lines.
# If keepends is True, then it returns the line breaks in the list.
# If keepends is False, then it removes the line breaks.
# defualt value of keepends is False.

# escape sequence for new line character is \n , \r  , \t , \b , \f , \v 
str ="aaa\nbbb\nccc\nddd"
print(str.splitlines()) # ['aaa', 'bbb', 'ccc', 'ddd']