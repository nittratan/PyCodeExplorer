# check the value lies in the given range or not

num = int(input("Enter a number: "))

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if num >= start and num <= end:
    print(f"The number {num} lies in the range {start} to {end}")
else:
    print(f"The number {num} does not lie in the range {start} to {end}")


# In the above program, we are checking whether the number lies in the given range or not. We are taking the number as input from the user and the start and end of the range. We are using the if-else statement to check whether the number lies in the given range or not. If the number lies in the range, we are printing that the number lies in the range. Otherwise, we are printing that the number does not lie in the range.

if range(start, end):
    print(f"The number {num} lies in the range {start} to {end}")

