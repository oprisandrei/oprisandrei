an= int(input("scrieti un an"))
if an%4==0 and not an%100==0 or  an%400==0:
    print("este un an bisect ")
else:
    print("nu este an bisect")