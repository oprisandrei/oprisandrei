nr=int(input("numar:"))

if nr%3==0 and nr%5==0:
    print("este divizibil cu 3 si 5")
elif nr%3==0:
    print("divizibil cu3")
elif nr%5==0:
    print("divizibil cu 5")
else:
    print("nue este divizibil cu nimic")