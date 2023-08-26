def verifica_an_bisect(an):
    if an%4==0 or an%100==0 and an%400==0:
        print(True)
    else:
        print(False)
    return an

print(verifica_an_bisect(2024))