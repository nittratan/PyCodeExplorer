# set internal working

"""

set internally uses hash table to store the elements. 
Hash table is a data structure which is used to store the elements in the form of key value pair. 
In set, elements are stored as keys and values are set to None. 
When we add elements in the set, it will store the elements in the hash table and set the value to None. 
When we try to add duplicate elements in the set, it will not store the duplicate elements in the hash table. 
It will store only distinct elements in the hash table. When we try to access elements in the set, it will check the hash table and return the elements. 
When we try to remove elements from the set, it will remove the elements from the hash table. When we try to remove elements which are not present in the set, 
it will throw an error. When we try to access elements using index, it will throw an error because set is unordered and unindexed.

"""

# hash function h(x) = x % 10
# Range of Hash Values: This hash function will produce hash values ranging from 0 to 9.
# Number of Buckets: You would need 10 buckets.
# Distribution: This might be suitable for smaller sets of data or when the data naturally clusters into fewer groups. However, 
# for larger datasets, the limited number of buckets might lead to more collisions, which can reduce performance.

# hash function h(x) = x % 16
# Range of Hash Values: This hash function will produce hash values ranging from 0 to 15.
# Number of Buckets: You would need 16 buckets.
# Distribution: This is generally better for larger datasets, providing more buckets to distribute elements and potentially reducing collisions.

# example
s = {10,20,30,40,50}
print(s) # {50, 20, 40, 10, 30} # order cab be different

s.add(60) # add() method is used to add elements in the set
print(s) # {50, 20, 40, 10, 60, 30}

s.add(18) # it will come after 50 
print(s) 

# in Hashing half of table filled then the size of table is increased