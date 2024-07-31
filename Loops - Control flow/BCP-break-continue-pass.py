# break , continue and pass statements in python

# break statement
# The break statement is used to terminate the loop containing it.


# A break statement will stop the loop then and there
# A break statement can be used in other loop situations as well apart frominfinite loop

while True: # infinite loop can never be terminated but by using break statement we can terminate it
    num = int(input("Enter the number: "))
    if num > 0:
        print("The number is positive")
    else:
        print("The number is negative")
        break

# if the user enters a negative number, the loop will terminate.


# continue statement

'''
Continue means it’ll not execute the rest of the loop it’ll simply go to beginning
of the loop and continue its execution

''' 


count = 0
while count < 10:
    n = int(input("Enter the number: "))
    if n%3 == 0:
        continue
    count += 1
    print(n)
    print("The number is not divisible by 3 ")
    

# pass statement

'''

Pass - In some cases when you don’t have to do anything use them just pass
the it
Pass means nothing to do
In python when you write a block of code you must write something if there’s
nothing to write , then simply write pass statement.

'''

count = 0
while count < 10:
    n = int(input("Enter the number: "))
    if n%3 == 0:
        pass
    count += 1
    print(n)
    print("The number is not divisible by 3 ")