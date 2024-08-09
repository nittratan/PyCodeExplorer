# country names 

country_names = {}

for i in range(4):
    names = input("Enter country name: ")
    if names[0].upper() not in country_names:
        country_names[names[0].upper()]=[names]
    else:
        country_names[names[0].upper()].append(names)

print(country_names)