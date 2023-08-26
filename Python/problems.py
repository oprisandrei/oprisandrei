#1.	Scrieti un program care afiseaza data curenta (plus ore, minute, secunde)
#2.	Scrieți un program Python pentru a afișa prima și ultima culoare din lista următoare.
#color_list = ["Red","Green","White" ,"Black"]
#3.	Scrieți un program Python care acceptă un întreg (n) și calculează valoarea n+nn+nnn.
#4.	Scrieți un program Python care va accepta baza și înălțimea unui triunghi și va calcula suprafața acestuia
import datetime as dt
text = input("Spune-mi un nr:")
print(text)
#1
x = dt.datetime.now()

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
#2
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])
#3
n = int(input("intreg:"))
print(n+(10*n+n)+((100*n)+(n*10)+n))
#4
b= float(input("baza:"))
h = float(input("inaltimea:"))
print(b*h/2)

