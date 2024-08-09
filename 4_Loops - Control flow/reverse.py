# reverse of a number

num = int(input("Enter the number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("The reverse of the number is: ", rev)
# input : Enter the number: 123
# The reverse of the number is: 321