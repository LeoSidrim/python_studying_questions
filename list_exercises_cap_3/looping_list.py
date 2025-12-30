for i in range(1,21): # Lista para exibir os 20 números.
    print(i)

numbers = []
#for number in range(1,1000001): # loop com 1 milhão de números
    #numbers.append(number) # Adiciono dentro da lista

for number in numbers:
    print(number)

#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))

for i in range(1,21,2): # Números ímpares de 1 a 21
    print(i)

three_numbers = []
for i in range(3,31,3):
    three_numbers.append(i)

for i in three_numbers:
    print(i)

cube_number = []
for i in range(1,11):
    cube_number.append(i**3)

for i in cube_number:
    print(i)

cubes_numbers = [i**3 for i in range(1,11)]
print(f"{cubes_numbers}  'List comprehension'")