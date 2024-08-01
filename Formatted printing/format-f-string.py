# placeholder in python 

# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.

# Syntax
# string.format(value1, value2...)

a = 22
b = 7
c = a/b

print('division of {0} and {1} is {2}'.format(a, b, c)) # 0 1 2 are the index of the values


# f string
# f-string is a new way to format strings in Python 3.6 and above.
# f-string is faster than other string formatting methods in Python.

# Syntax
# f'{value}'
# f'{value1} {value2}'
# f'{value1} {value2} {value3}'
# f'{expression}'
# f'{expression1} {expression2}'
# f'{expression1} {expression2} {expression3}'
# f'{variable}'
# f'{variable1} {variable2}'

a = 22
b = 7
c = a/b


print(f'division of {a} and {b} is {c}') # f string
print(f'division of {a} and {b} is {c:.2f}') # f string with 2 decimal places

"""
f-string :

An f-string (formatted string literal) is a concise and convenient way to embed 
expressions inside string literals using curly braces {}. Introduced in Python 3.6, f-strings provide 
a readable and intuitive way to format strings.

"""