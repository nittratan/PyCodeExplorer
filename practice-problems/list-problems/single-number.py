# Given a list of integers, concatenate the integers in the list to form a single number.

list1 = [1,2,3,4,5,6,7,8,9]

# convert the list of integers to a list of strings
str_list = [str(i) for i in list1]

# concatenate the strings in the list
result = "".join(str_list)
print(result)

# another way
result = ''
for x in list1:
    result += str(x)

print(int(result)) # 123456789

