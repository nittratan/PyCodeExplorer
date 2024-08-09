# birthday of person

# input: name

# output: name, age, birth year, birth month, birth date

birthday = {
    "Raju" : '1996-12-12',
    'Sumit' : '1998-05-12',
    'Rahul' : '1995-06-21',
    'Rohit' : '1997-07-22',
    'Raj' : '1999-08-23',
    'Sachin' : '1994-09-24',
    'Ravi' : '1993-10-25',
    "Kishan": '1992-11-26'

}

name = input("Enter name: ").title()
dob = birthday.get(name , 'not found')
print(f" Date of birth of {name} is {dob} ")

print(dir(input))