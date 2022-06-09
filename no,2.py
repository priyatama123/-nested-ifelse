from winreg import EnableReflectionKey


age=int(input("enter age"))
gender=input("enter gender")
m_s=input("enter m_s")
if gender=="f":
    if age>=20 and age<=60:
        print("she will work only in urban area")
    else:
        print("error")
elif gender=="m":
    if age>=20 and age<=40:
        print("he may work in any where")
    elif age>=40 and age<=60:
        print("he will work in urban area")
    else:
        print("error")      
else:
    print("error")              
