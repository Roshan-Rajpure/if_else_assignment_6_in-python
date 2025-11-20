purchase_amount = float(input("Enter purchase amount: "))

discount_percentage = 0

if purchase_amount < 1000:
    discount_percentage = 0
elif purchase_amount <= 4999:
    discount_percentage = 5
elif purchase_amount <= 9999:
    discount_percentage = 10
elif purchase_amount <= 19999:
    discount_percentage = 20
else:
    discount_percentage = 30

discount_value = (purchase_amount * discount_percentage) / 100
final_amount = purchase_amount - discount_value

print(f"Discount Applied: {discount_percentage}%")
print(f"Final Amount: ₹{final_amount}")