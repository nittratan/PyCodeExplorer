'''
String is a collection of alphabets which is used for making a word or a sentence or a paragraph whichis most commonly used data in programming languages.

Python is having a built in class available for string.


'''

# Python strings are "immutable" which means they cannot be changed after they are created.

"""*********************Important thing************************

So a string is a immutable object.

Once we have created a string, it cannot be modified.

If you are modifying it, then with the modification a new string will be created."""

# single line string
s1 = 'Hello' # single quotes allowed
s2 = "Hello" # double quotes allowed

# s3 ="hello' # not allowed

# multi line string
str = '''
 Hello
 How are you ?
 I am fine
 what about you ?
 what's going on ?
 what's your name ?

    '''
print(str)



str1 = "Hello"

print(str1)
print(type(str1))
print(str1[0])
print(str1[-1])

for s in str1:
    print(s)

s2 ="Welcome"
for char in s2:
    print(char,end='')

print("\n") # new line

# length of string
print(len(str1))

