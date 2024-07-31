# check given password and confirm password are same or not

pass1 = input("Enter password: ")
pass2 = input("Confirm password: ")

if pass1 == pass2:
    print("Password is confirmed.")
else:
    if pass1.casefold() == pass2.casefold(): # casefold() method converts the string to lowercase and remove all case distinctions. 
        print("Please check for the cases .")
    else:
        print("Password is not confirmed.")
