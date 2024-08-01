# print function in python

# print(object , sep=' ', end='\n', file=sys.stdout, flush=False)

# object : Any object, will be converted to string before printed
# sep : separator between objects, default is space
# end : end of line, default is new line
# file : file object where output will be printed default is sys.stdout

""" 
end is a parameter in print() function. By default, 
end is set to '\n' which means the cursor will move to the next line after printing the output.
You can change this behavior by passing end parameter.
"""

print("Hello World")
print("Hello", "World")

a = 10
b = 20
c = 30
print(a, b, c)
print(a, b, c, sep=" | ")

print("Hello", end=" ")
print("World")

