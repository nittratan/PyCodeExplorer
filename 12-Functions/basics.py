# Creating a Function :
# Syntax : 
# def function_name(parameters):
#   """docstring""" # docstring is used to describe the function [optional]
#   statement(s)
#   return value

# A function must return a result and it python it returns result
# f you don’t write return inside a function then it’ll automatically returns None

def msgFun():
    """
    This is a function that prints a message
    """

    return {"message": "Hello World!"}

print(msgFun()) # Output: {'message': 'Hello World!'}

def myFun():
    """
    This is a function that does nothing
    """

# In python, function always return a value. If no return statement is given, it returns None.


print(myFun())

# Output: None

def myFun1():
    """
    This is a function that does nothing
    """
    pass # pass is used here to avoid syntax error

print(myFun1()) # Output: None

def add(a, b):
    print("inside function" , id(a), id(b))

x, y = 5, 6
print("outside function" , id(x), id(y))

print(add(x, y)) # Output: None


def add3(a, b, c):
    """
    This is a function that adds three numbers
    """
    res = a + b + c
    return res


add3(11, 22, 33)  # skipped the return value of the function because it is not stored in a variable or used in a print statement 
'''
    Return Value is Ignored: When you call a function that returns a value, and you don't store the 
    result or use it (e.g., in a print statement), the return value is simply discarded. 
    The program continues executing without any issues.
'''

res = add3(1, 2, 3) 
print(res) # Output: 6

'''
    When calling a function that returns a result, you have two main options for handling that result: 
    storing it in a variable or directly using it 

'''