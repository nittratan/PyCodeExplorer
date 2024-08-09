# Nested List
# A list can have heterogeneous type of elements, like it can have integer float or a complex number.

# A list can also have another list as an element. This is called a nested list.

# create matrix using nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0]) # [1, 2, 3]
print(matrix[1]) # [4, 5, 6]

# create matrix 

mat = []
for i in range(5):
    mat.append([]) # append an empty list before adding elements to it
    for j in range(5):
        mat[i].append(j)

print(mat)

# print matrix
for i in range(5):
    for j in range(5):
        print(mat[i][j],end=" ")
    print()