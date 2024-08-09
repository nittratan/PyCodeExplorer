# conditional statements 

# conditional statements are used to execute a block of code based on a condition
# conditional statements are used to make decisions
# conditional statements are used to perform different actions based on different decisions
# conditional statements are used to control the flow of the program
# conditional statements are used to check whether a condition is true or false
# conditional statements are used to perform different actions based on different conditions

# types of conditional statements
# if statement
# if statement is used to execute a block of code if a condition is true

# syntax of if statement
# if condition:
#     block of code

# if statement example
# check whether a number is positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")

# if-else statement
# if-else statement is used to execute a block of code if a condition is true and another block of code if the condition is false

# syntax of if-else statement
# if condition:
#     block of code
# else:
#     block of code

# if-else statement example
# check whether a number is positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is negative")

# if-elif-else statement
# if-elif-else statement is used to execute a block of code if a condition is true, another block of code if another condition is true, and another block of code if all the conditions are false

# syntax of if-elif-else statement
# if condition:
#     block of code
# elif condition:
#     block of code
# else:
#     block of code

# if-elif-else statement example
# check whether a number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")