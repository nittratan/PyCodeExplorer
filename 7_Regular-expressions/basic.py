# A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or set of strings.

import re

# re.match() function returns a match object on success, None on failure
# re.match(pattern, string, flags=0)
# pattern: regular expression to be matched
# string: string to be searched to match the pattern at the beginning of the string
# flags: different flags can be passed to match the pattern

print(re.match('www', 'www.google.com'))  # <re.Match object; span=(0, 3), match='www'>

print(re.match('com', 'www.google.com'))  # None (pattern not found at the beginning of the string)

# re.search() function returns a match object on success, None on failure
# re.search(pattern, string, flags=0)

print(re.search('com', 'www.google.com'))  # <re.Match object; span=(11, 14), match='com'>


# re.findall() function returns a list of all matches
# re.findall(pattern, string, flags=0)

print(re.findall('com', 'www.google.com'))  # ['com']

# re.split() function splits the string where there is a match and returns a list of strings where the splits have occurred
# re.split(pattern, string, maxsplit=0, flags=0)

print(re.split('\.', 'www.google.com'))  # ['www', 'google', 'com']

# re.sub() function replaces one or many matches with a string
# re.sub(pattern, repl, string, count=0, flags=0)

print(re.sub('\.', '-', 'www.google.com'))  # www-google-com