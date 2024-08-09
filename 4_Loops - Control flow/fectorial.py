# fectorial of a number

num = int(input("Enter the number: "))
fectorial = 1
for i in range(1, num+1):
    fectorial *= i

print(fectorial)
