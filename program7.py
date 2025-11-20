percentage = float(input("enter percentage: "))
score = float(input("enter score: "))

if score >= 90 and percentage >= 90:
    print("elite program")
elif score >= 70 and percentage >= 70:
    print("standard program")
elif score >= 50 and percentage >= 50:
    print("basic program")
else:
    print("Not eligible")