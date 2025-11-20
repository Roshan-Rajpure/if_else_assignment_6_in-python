unit = int(input("enter units : "))

if(unit<=100):
    ans= unit*5
    print("total bill is : ",ans)
elif(100<=unit<=200):
    ans= unit*7
    print("total bill is : ",ans)
elif(200<=unit<=300):
    ans= unit*10
    print("total bill is : ",ans)
else:
    ans=unit*15
    print("total bill is : ",ans)
