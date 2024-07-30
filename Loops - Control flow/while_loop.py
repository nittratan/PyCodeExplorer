#  While loop
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

# Output: 1 2 3 4 5 6 7 8 9 10

# print hello world ! 10 times
i = 1
while i <= 10:
    print("Hello World !")
    print(i)
    i = i + 1 # if we comment this line then the loop will run infinitely


