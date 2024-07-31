# calculate discount for a given order

bill_amount = int (input("Enter the bill amount: "))

if bill_amount < 500:
    discount = 0.05 * bill_amount
    # 5% discount
    print(f"Discount: {discount}")
    print(f"Amount to be paid: {bill_amount - discount}")
elif bill_amount >= 500 and bill_amount < 1000:
    discount = 0.1 * bill_amount
    # 10% discount
    print(f"Discount: {discount}")
    print(f"Amount to be paid: {bill_amount - discount}")
else:
    discount = 0.15 * bill_amount
    # 15% discount
    print(f"Discount: {discount}")
    print(f"Amount to be paid: {bill_amount - discount}")