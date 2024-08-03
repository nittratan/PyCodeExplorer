# Given a list of weekly hours, calculate the weekly salary of an employee. 

work_hours = [8,6,8,6,9]

# The salary is calculated as follows:
# sum of weekly hours * hourly rate

hourly_rate = 100

sum_hours = 0

for i in work_hours:
    sum_hours += i

weekly_salary = sum_hours * hourly_rate

print(f"weekly_salary: {weekly_salary}")

hours = input("Enter the weekly hours: ").split() # it will split the input string into a list of strings

# convert the list of strings to a list of integers
print(hours)

for i in work_hours:
    sum_hours += int(i)

weekly_salary = sum_hours * hourly_rate
print(f"weekly_salary: {weekly_salary}")