n=int(input("un numar"))

suma=0

while n>0:
    suma+=n%10
    n=n//10

print(suma)
