sir=str(input("sir de caractere:"))
sir2=str(input("sir 2:"))

a =sorted(list(sir))
b=sorted(list(sir2))

print(a)
print(b)

if a==b:
    print("este anagrama")
else:
    print("nu este anagrama")