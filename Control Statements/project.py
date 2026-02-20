age = int(input("Enter Your Age: "))
if age>0 and age<=1:
    print("Infant")
elif age>1 and age<=3:
    print("Toddler")
elif age>3 and age<=6:
    print("Early Childhood")
elif age>6 and age<=12:
    print("Middle Childhood")
elif age>12 and age<=19:
    print("Teenager")
elif age>19 and age<=35:
    print("Young Adult")
elif age>35 and age<=55:
    print("Middle Adult")
elif age>55 and age<=65:
    print("Senior Adult")
elif age>65 and age<=80:
    print("Old Age")
else:
    print("Invalid Age")



