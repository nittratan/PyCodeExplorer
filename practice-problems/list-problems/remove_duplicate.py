# remove duplicate from given list

myList = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print(myList)

tempList = []

for x in myList:
    if x not in tempList:
        tempList.append(x)

print(tempList)

# using sort()
myList.sort()
print(myList)

# Remove duplicates in place
i = len(myList) - 1
while i > 0:
    if myList[i] == myList[i - 1]:
        myList.pop(i)
    i -= 1

print(myList)