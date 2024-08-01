card = input("Input card number: ")

lastDigit = card[15::]

four = '*' * 4

print(f"Card details: {four*3} {lastDigit}")

# card 1234 5678 9012 3456
# Card details: **** **** **** 3456