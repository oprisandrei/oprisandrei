def valoare_cheie(dictionar,cheie):
    try:
        return dictionar[cheie]
    except KeyError:
        return "cheia nu exista"
        pass
def valoare_cheie2(dictionar,cheie):
    if cheie in dictionar:
        return dictionar[cheie]
    else:
        return "Cheia nu exista"

def valoare_cheie3(dictionar,cheie):
    return dictionar.get(cheie,"Cheia nu exista")



print(valoare_cheie({"a":1,"b":2,"c":3},"b"))
valoare_cheie({"a":1,"b":2,"c":3},"a")
print(valoare_cheie({"a":1,"b":2,},"c"))

print(valoare_cheie2({"a":1,"b":2,"c":3},"b"))
valoare_cheie({"a":1,"b":2,"c":3},"a")
print(valoare_cheie2({"a":1,"b":2,},"c"))

print(valoare_cheie3({"a":1,"b":2,"c":3},"b"))
valoare_cheie({"a":1,"b":2,"c":3},"a")
print(valoare_cheie3({"a":1,"b":2,},"c"))
