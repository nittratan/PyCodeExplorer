# Loops are useful for repeatedly executing set of statements.
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

# Syntax of for Loop
# for val in sequence:
#     Body of for
# Here, val is the variable that takes the value of the item inside the sequence on each iteration.

msg = "Hello"
for m in msg:
    print(m)

# It repeats for each character in the string. so this loop is called for each loop.

# It is also possible to iterate over a sequence of numbers using the range function.
# What is Range?
# Range is a function
# Suppose range(10) 0,1,2,3,4,5,6,7,8,9 it will stop at just one number before the last number.
# If you give range(5,10) start = 5  ..... and end = 9         5,6,7,8,9

# range(start, stop, step) # start is optional, stop is required, step is optional
# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.

for i in range(5):
    print(i,end=" ")

for i in range(5, 10):
    print(i,end=" ")

for i in range(0, 10, 2):
    print(i,end=" ")

for i in range(10, 0, -1): # reverse order
    print(i,end=" ")

# for each in the range print will be executed.