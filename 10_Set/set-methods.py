# set methods

# union(iterable)
# intersection(iterable)
# intersection_update(iterable)
# difference(iterable)
# difference_update(iterable)
# symmetric_difference(iterable)
# symmetric_difference_update(iterable)

s1 = {1,2,3,5,7}
s2 = {5 , 7, 9, 10 , 11}

# union
s3 = s1.union(s2)
print(s3) # {1, 2, 3, 5, 7, 9, 10, 11} # union of two sets

# intersection
s4 = s1.intersection(s2)
print(s4) # {5, 7} # common elements in both sets

# intersection_update
s1.intersection_update(s2)
print(s1) # {5, 7} # common elements in both sets

# difference
s5 = s2.difference(s1)
print(s5) # {9, 10, 11} # elements present in s2 but not in s1

# difference_update
s2.difference_update(s1)
print(s2) # {9, 10, 11} # elements present in s2 but not in s1

# symmetric_difference
s6 = s1.symmetric_difference(s2)
print(s6) 

# symmetric_difference_update
s1.symmetric_difference_update(s2)
print(s1) 
