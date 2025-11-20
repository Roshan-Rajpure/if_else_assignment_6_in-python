char = input("enter character : ")

if('a'<=char<='z'):
    print("lowercase letter ")
elif('A'<= char <= 'B'):
    print("uppercase letter ")
elif('0'<=char <='9'):
    print("digit")
else:
    print("special character ")