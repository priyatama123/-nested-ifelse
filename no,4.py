day=input("enter day")
meal_time=input("enter meal_time")
if day=="monday":
    if meal_time=="breakfast":
        print("poori sabzi")
    elif meal_time =="lunch":
        print("sambhar rice")
    elif meal_time=="dinner":
        print("chicken rice")
    else:
        print("no meal") 
elif day=="tuesday":
    if meal_time=="breakfast":
        print("poha")
    elif meal_time=="lunch":
        print("rajma rice")
    elif meal_time=="dinner":
        print("roti sabzi")
    else:
        print("not meal")
else:
    print("none")  


