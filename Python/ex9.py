age=int(input("varsta:"))

if age>=0 and age<=12:
    print("Esti copil")
elif age>=13 and age <=19:
    print("Esti un adolescent")
elif age >=20 and age<=59:
    print("Esti un adult")
elif age>=60:
    print("Esti un senior")