peoples = ['Jesus', 'Débora', 'Silva', 'Vladimir', 'Matheus', 'Lucas']

print(f'{peoples[0]} gostaria de jantar comigo?')
print(f'{peoples[1]} gostaria de jantar comigo?')
print(f'{peoples[2]} gostaria de jantar comigo?')
print(f'{peoples[3]} gostaria de jantar comigo?')
print(f'{peoples[4]} gostaria de jantar comigo?')
print(f'{peoples[5]} gostaria de jantar comigo?')

print(peoples[3])
del peoples[3] # Deleta elemento pelo índice 

peoples.append('Marcus') # Adiciona elemento no final da lista
print(f'{peoples[5]} gostaria de jantar comigo?')


peoples.insert(0,'Tiago') # Insere um elemento na lista no índice indicado (todos os outros elemento andam um passo)
peoples.insert(3,'Pedro')
peoples.append('João')

print('Posso somente convidar 2 pessoas para o jantar.')
first_person = peoples.pop()
print(f'Peço perdão {first_person}, mas posso somente chamar 2 pessoas para meu jantar.')
second_person = peoples.pop()
print(f'Peço perdão {second_person}, mas posso somente chamar 2 pessoas para meu jantar.')
third_person = peoples.pop()
print(f'Peço perdão {third_person}, mas posso somente chamar 2 pessoas para meu jantar.')
fourth_person = peoples.pop()
print(f'Peço perdão {fourth_person}, mas posso somente chamar 2 pessoas para meu jantar.')
fifth_person = peoples.pop()
print(f'Peço perdão {fifth_person}, mas posso somente chamar 2 pessoas para meu jantar.')
sixth_person = peoples.pop()
print(f'Peço perdão {sixth_person}, mas posso somente chamar 2 pessoas para meu jantar.')
seventh_person = peoples.pop()
print(f'Peço perdão {seventh_person}, mas posso somente chamar 2 pessoas para meu jantar.')

print(f'{peoples[0]} você ainda está convidada')
print(f'{peoples[1]} você ainda está convidada')

del peoples[0] # tive que usar o mesmo índice, pois removi e todos andaram uma para esquerda
del peoples[0]
print(peoples)