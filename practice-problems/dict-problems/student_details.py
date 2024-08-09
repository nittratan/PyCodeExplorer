# given a student name print the details of that student.

std_details = {
    'Raju' : {
        'age' : 25,
        'city' : 'Patna',
        'roll' : 101,
        'class' : 'B.Tech'
    },
    'Rahul' : {
        'age' : 24,
        'city' : 'Delhi',
        'roll' : 102,
        'class' : 'M.Tech'
    },
    'Kishan' : {
        'age' : 23,
        'city' : 'Mumbai',
        'roll' : 103,
        'class' : 'MCA'
    },
    'Shivam' : {
        'age' : 22,
        'city' : 'Bangalore',
        'roll' : 104,
        'class' : 'MBA'
    },
    'Ravi' : {
        'age' : 21,
        'city' : 'Chennai',
        'roll' : 105,
        'class' : 'BBA'
    }
}

name = input("Enter student name: ").title()
details = std_details.get(name, 'Student not found')
print(details)

