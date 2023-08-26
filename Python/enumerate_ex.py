elemente=["mere","creion","masina","pix","ceas","laptop"]

for element in elemente:
    print(element,elemente.index(element)+1)

for index in range(len(elemente)):
    print(index+1,elemente[index])

#enumerate

for index,element in enumerate(elemente,start=1):
    print(index,element)

print(enumerate(elemente,start=1))

