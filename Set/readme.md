## How set internally work

``Python sets are implemented using hash tables, which provide an efficient way to store and retrieve unique items. Here's a breakdown of how sets work internally: ``

**Hash Tables**

*Hashing*: When an element is added to a set, its value is passed through a hash function, which computes an integer called the hash value. This hash value is used as an index to store the element in an internal array (the hash table).

*Buckets*: The internal array consists of multiple buckets. Each bucket can hold one or more elements. Ideally, each element will be placed in a unique bucket based on its hash value.

*Collisions*: When two elements have the same hash value (a collision), they are stored in the same bucket. Python handles collisions using linked lists or other structures to manage multiple elements in a single bucket.

*Unique Elements*: Since sets only store unique elements, Python checks if the element already exists in the set before adding it. This check is also done using the hash value and the bucket where the element would be stored.

*Operations*
Adding Elements: To add an element, Python computes its hash value and places it in the appropriate bucket. If the element already exists in the set, it is not added again.

*Removing Elements*: To remove an element, Python computes its hash value to find the appropriate bucket and then removes the element from that bucket.

*Checking Membership*: To check if an element is in the set, Python computes its hash value and looks in the corresponding bucket to see if the element is present.

**Efficiency**
#### Average Time Complexity:

Adding an element: 
- Adding an element: O(1)
- Removing an element: O(1)
- Checking membership: O(1)

These operations are efficient on average because accessing a bucket using a hash value is a constant-time operation.

