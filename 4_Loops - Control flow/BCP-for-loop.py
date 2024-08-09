# break , continue , pass with for loop

for i in range(10):
    if i>5:
        break
    else:
        print(i)

# once i becomes greater than 5, the loop will break and the program will exit the loop.

# for else loop
for i in range(10):
    print(i)
else:
    print("for completed successfully")


for i in range(10):
    if i==5:
        break
    else:
        print(i)
else:
    print("for completed successfully")

# here else blocked will not printed because loop is breaked before completion.


# pass statement
for i in range(10):
    pass

# pass statement is used when you don't want to do anything in the loop. It is used as a placeholder for future code. 
# if we not pass then it's give error because it's empty block. Error : IndentationError: expected an indented block

# continue statement

for i in range(10):
    if i%5==0:
        continue
    print(i)
