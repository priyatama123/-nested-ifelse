year=int(input("enter year"))
if year%4==0 and year%400==0:
    if year%100==0 and year%400==0:
        print("it is leap year")
    else:
        print("it is leap year")
else:
    print("not leap year")
