str = 'csavbcda'

# sorted() => this returns a list of sorted characters
sorted_str = sorted(str)
print(sorted_str) # ['a', 'a', 'b', 'c', 'c', 'd', 's', 'v']

# join() => this joins the sorted characters to form a string
sorted_str = ''.join(sorted_str)
print(sorted_str) # aabccdsv