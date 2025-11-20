print("Enter three angles:")
angle1 = float(input())
angle2 = float(input())
angle3 = float(input())

if (angle1 + angle2 + angle3) != 180:
    print("Invalid Triangle")
else:
    if angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Triangle is Obtuse")
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("Triangle is Acute")
    else:
        print("Triangle is Right")