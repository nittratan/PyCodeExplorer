# check pass or fail on the basis of marks

math = int(input("Enter the marks obtained in Mathematics: "))
science = int(input("Enter the marks obtained in Science: "))
english = int(input("Enter the marks obtained in English: "))

if math >= 35 and science >= 35 and english >= 35:
    print("Congratulations! You have passed the exam")
else:
    print("Sorry! You have failed the exam")