# area of triangle

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
# input() returns a string, so we need to convert it to a float / int otherwise we will get a TypeError
area = 0.5 * base * height
print(f"The area of the triangle is {area}")