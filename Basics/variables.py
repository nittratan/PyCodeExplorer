# rules for naming/declaring variables

# without assigning a value to a variable, it will throw an error and we can't declare a variable without assigning a value
# 1. Variable names must start with a letter or an underscore
# 2. Keywords can't be used as variable names
# 3. Variable names can't contain special characters like @, $, %, etc.
# 4. Variable names can't contain spaces
# 5. Variable names are case-sensitive

# Variable assignment
a = 50

# Variable reassignment
a = 100

# Multiple assignment
a, b, c = 5, 10, 15

# Assign the same value to multiple variables
a = b = c = 10

roll_no = 115
price = 5.5
cust_name = 'John'

# print multiple variables
print(roll_no, price, cust_name)

address = 'Patna' # allowed
# address@ = 'Patna' # not allowed
# 1address = 'Patna' # not allowed
# address 1 = 'Patna' # allowed

_value = 10 # allowed
value_ = 10 # allowed

_145val = 10 # not allowed
