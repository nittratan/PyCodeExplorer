# Overlapping Elements in Two Lists

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

# Find the overlapping elements in the two lists
lst3 = []
for x in lst1:
    if x in lst2:
        lst3.append(x)

print(lst3) # [4, 5]

