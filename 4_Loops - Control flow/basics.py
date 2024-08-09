# Loops - Control flow

'''

Control flow is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated.

If you want a set of statements to repeat again and again in the program then we use loops
The statements can repeat either ‘for number of times’ or ‘As long as the condition is true’

There are two types of loops in Python:
1. while loop
2. for loop


'''

# While loop
# The while loop is used to iterate over a block of code as long as the test expression (condition) is true.
# The test expression is given inside the parenthesis ().
# The body of the loop is indented.


# control flow / daigram of while loop 

# Syntax:
# while test_expression:
#     Body of while

# example
# Program to print 1 to 10 using while loop
# initialize the variable i to 1
i = 1
# while loop with condition i less than or equal to 10
while i <= 10:
    # print the value of i
    print(i , end = ' ')
    # increment the value of i by 1
    i = i + 1
