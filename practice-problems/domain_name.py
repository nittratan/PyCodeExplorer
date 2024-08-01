# extract domain name from email id

email = input("Enter email id: ")

atrate = email.find("@") # find() method returns the index of first occurrence of substring.

print(atrate)

print("User Id: ",email[:atrate]) # extract user id from email id using slicing

print("Domain Name: ",email[atrate+1:]) # extract domain name from email id using slicing


# extract domain name from email id using split() method
email = input("Enter email id: ")
domain = email.split("@") # split() method splits the string into a list of substrings.
print("User Id: ",domain[0]) # extract user id from email id using list indexing
print("Domain Name: ",domain[1]) # extract domain name from email id using list indexing


# replace domain name
email = "sratan@gmail.com"
new_email = email.replace("gmail.com","nitt.edu")
print(new_email) # sratan@nitt.edu

email ="sratan338@gmail.com"
print(email.replace("gmail","yahoo")) # sratan338@yahoo.com
