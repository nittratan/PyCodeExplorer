# Given a list of characters, find the number of occurrences of each item in the list.

lstStr = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'E', 'F', 'E', 'G', 'H']

result = []

for i in lstStr:
    if i not in result:
        result.append(i)

for i in result:
    print(i, lstStr.count(i))

# Another way to solve the problem
res = []

for item in lstStr:
    if item not in res:
        res.append(item)
        count = lstStr.count(item)
        res.append(count)

print(res)
    