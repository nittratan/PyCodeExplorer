# list methods
# member functions that present in list class are called list methods

# print(dir(list))
# print(help(list))

# append() : appends an element at the end of the list
# extend() : extends the list by appending elements from the iterable
# insert() : inserts an element at the specified position
# remove() : removes the first occurrence of the element with the specified value
# pop() : removes the element at the specified position
# clear() : removes all the elements from the list
# index() : returns the index of the first element with the specified value
# count() : returns the number of elements with the specified value
# sort() : sorts the list
# reverse() : reverses the order of the list
# copy() : returns a copy of the list

# append(val)
myList =[7,12,9,13,15,11]
print(myList)
print(len(myList))
myList.append(20)
print(myList)
print(len(myList))

# myList.append(30,50) # TypeError: append() takes exactly one argument (2 given)
# new list size = 7
# new list = [7, 12, 9, 13, 15, 11, 20]

# append using slicing
myList[8:8]=[25] # mylist[len(myList):] = [25] # append at the end
print(myList)

# extend(iterable)
lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.extend(lst2)
print(lst1) # [1, 2, 3, 4, 5, 6]
lst2.extend([7,8,9])
print(lst2) # [4, 5, 6, 7, 8, 9]

# insert(index, val) : inserts an element at the specified position
# index must be in the range of 0 to len(lst)

lst = [1,2,3,4,5]
print(lst)
print(len(lst))
lst.insert(2, 100)
print(lst) # [1, 2, 100, 3, 4, 5]
lst.insert(0, 200)
print(lst) # [200, 1, 2, 100, 3, 4, 5]
lst.insert(len(lst), 300)
print(lst) # [200, 1, 2, 100, 3, 4, 5, 300]


# copy() : returns a copy of the list
# shallow copy
lst = [1,2,3,4,5]
print(lst)
lst1 = lst.copy()
print(lst1)
lst1[0] = 100
print(lst1)
print(lst)

# id function : returns the memory address of the object
print(id(lst))
print(id(lst1))

# pop() , remove() ,clear() => these methods are used to remove elements from the list

# pop() : removes the element at the specified position
# if no index is specified, it removes the last element 
# index is optional
# if the index is out of range, it throws an IndexError
lst = [1,2,3,4,5]
print(lst)
print(len(lst))
lst.pop()
print(lst) # [1, 2, 3, 4]
print(len(lst))

lst.pop(1) # removes the element at index 1
print(lst) # [1, 3, 4]


# remove() : removes the first occurrence of the element with the specified value
# if the element is not present in the list, it throws a ValueError
lst = [1,2,3,4,5]
print(lst)
print(len(lst))
lst.remove(3)
print(lst) # [1, 2, 4, 5]
print(len(lst))

# lst.remove(10) # ValueError: list.remove(x): x not in list

# clear() : removes all the elements from the list

lst = [1,2,3,4,5]
print(lst)
print(len(lst))
lst.clear()
print(lst) # []
print(len(lst))

list1 = [1,2,3,4,5]
del(list1[:]) # del(list1) # deletes the list object 
print(list1) # []

# index() , count() , sort() , reverse() => these methods are used to search, sort and reverse the list

# index() : returns the index of the first element with the specified value
# if the element is not present in the list, it throws a ValueError
lst = [1,2,3,4,5]
print(lst)
print(lst.index(3)) # 2
print(lst.index(5)) # 4
# print(lst.index(10)) # ValueError

# count() : returns the number of elements with the specified value
# count all the occurrences of the element in the list
# if the element is not present in the list, it returns 0
lst = [1,2,3,4,3,5,3]
print(lst)
print(lst.count(3)) # 3
print(lst.count(10)) # 0

# reverse() : reverses the order of the list
lst = [1,2,3,4,5]
print(lst)
lst.reverse()
print(lst) # [5, 4, 3, 2, 1]

# sort() : sorts the list
# sort(*, key=None, reverse=False)
# key : function that will be used to sort the elements
# reverse : True => descending order, False => ascending order default is False

lst = [5,2,5,3,6,7,4,4,10,9,2,1]
print(lst)
lst.sort()
print(lst) # [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 9, 10]
lst.sort(reverse=True)
print(lst) # [10, 9, 7, 6, 5, 5, 4, 4, 3, 2, 2, 1]

# sort() with key
l1 = ['YY','jj','mm','BB','aa','zz'] # upper case letters have lower ASCII values
print(l1)
l1.sort()
print(l1) # ['BB', 'YY', 'aa', 'jj', 'mm', 'zz']
l1.sort(key=str.lower) # case insensitive sort 
print(l1) # ['aa', 'BB', 'jj', 'mm', 'YY', 'zz']
