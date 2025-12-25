friends = ['Matheus', 'Lucas', 'Débora', 'Jadson'] # Criei a lista com nome dos meus amigos
print(friends[0])
print(friends[1]) # Acessei a lista e printei o nome um por um
print(friends[2])
print(friends[3])
friends.insert(0,'Silvia') # Adiciona o elemento no index desejado
print(friends)
friends.append('Isaac') # Adiciona no final da lista
del friends[0] # Deleta o elemento no index desejado.
print(friends)
popped_friend = friends.pop() # Armazena o elemento e pode ser iterado em uma variável, para ser utilizado depois.
print(friends)
print(popped_friend)
print(len(friends)) #informa o tamanho da lista