numbers=[]
for i in range(50):
    numbers.append(i)
print(numbers)

numbers=[i for i in range(50)]
print(numbers)

even_numbers=[]
for i in range(50):
    if i%2==0:
        even_numbers.append(i)
print(even_numbers)

even_numbers=[i for i in range(50) if i%2==0]
print(even_numbers)


power_numbers=[]

for number in range(50):
    if number%2==0:
        power_numbers.append(number**2)
    else:
        power_numbers.append(number**3)
print(power_numbers)



power_numbers=[number**2 if number%2==0 else number**3 for number in range(50)]
print(power_numbers)



#numevariabila=[elem_lista for elem_care _se_adauga in iterabil]
