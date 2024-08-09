# dictionary methods

# copy() 
# update()
# setdefault(key,value) -> setdefault(key , [default_value]) [] means optional
# formkeys(seq, value) -> formkeys(seq, [value]) [] means optional

# copy() 
dict1 = {'name':'Raju', 'age':25, 'city':'Patna'}
dict2 = dict1.copy()
print('dict1:',dict1)
print('dict2:',dict2)

dict2['name'] = 'Rahul'
print(dict2)

print(id(dict1['age']))
print(id(dict2['age']))
# both have same id because they are different objects but have same value 

dict3 = {'roll':101, 'class':'B.Tech'}

dict1.update(dict3)
print('dict1:',dict1)

# setdefault(key,value) -> setdefault(key , [default_value]) [] means optional
# if key is present then return the value of that key otherwise set the key with default value 
dict4 = {'name':'Raju', 'age':25, 'city':'Patna'}
print(dict4.setdefault(13421)) # key is not present so it will set the key with default value None
# key = 13421, value = None
print(dict4.setdefault('110','roll')) # 
print(dict4)

# formkeys(seq, value) -> formkeys(seq, [value]) [] means optional
# seq = sequence of elements 
# value = value of each key
# it will return a dictionary with keys from seq and value of each key is value
l1 = [10,20,30,40]
dict5 = {}
print(dict5.fromkeys(l1))
print(dict5.fromkeys(l1, 'roll')) # value of each key is roll


# pop(key,defaul) -> it will remove the key and return the value of that key
# if key is not present then it will return the default value
# if default value is not present then it will raise an error
dict6 = {'name':'Raju', 'age':25, 'city':'Patna'}
print(dict6.pop('name')) # it will remove the key name and return the value of that key
print(dict6)
print(dict6.pop('roll','key is not present')) # key is not present so it will return the default value
# print(dict6.pop('roll')) # key is not present so it will raise an error

# popitem() -> it will remove the last key-value pair from the dictionary
dict7 = {'name':'Raju', 'age':25, 'city':'Patna'}
print(dict7.popitem())
print(dict7)

# clear() -> it will remove all the key-value pairs from the dictionary
dict8 = {'name':'Raju', 'age':25, 'city':'Patna'}
dict8.clear()
print(dict8)


