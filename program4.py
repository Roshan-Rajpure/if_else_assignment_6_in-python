income = float(input("Enter income: "))

tax = 0.0

if income <= 250000:
    tax = 0.0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (income - 250000) * 0.20

elif income > 1000000:
    tax = (income - 250000) * 0.30

print(f"Tax to be paid: ",tax)