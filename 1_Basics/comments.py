# comments in python

# comments are used to make code more readable
# comments are ignored by the python interpreter
# comments are used to explain the code
# comments are used to prevent execution when testing code

# single line comment
# this is a single line comment
# print("Hello World")

# multi line comment
'''

this is a multi line comment

print("Hello World")

'''

# docstring
# docstring is a string literal that occurs as the first statement in a module, function, class, or method definition
# docstring is used to document the code

def add(a, b):
    '''

    This function takes two arguments and returns their sum

    '''
    return a+b

print(add(10, 20))

print(add.__doc__) # to print docstring of a function

