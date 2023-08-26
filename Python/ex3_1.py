x=int(input("numar"))
if x>0:
    if x%2==0:
        print("este pozitiv si par")
    else:
        print("este pozitiv si impar")
elif x<0:
    if x%2==0:
        print("numarul este negativ si par")
    else:
        print("este negativ si impar")
else:
    print("numarul este zero")