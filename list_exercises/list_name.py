friends = ['Matheus', 'Lucas', 'Débora', 'Jadson'] # Criei a lista com nome dos meus amigos
print(friends[0])
print(friends[1]) # Acessei a lista e printei o nome um por um
print(friends[2])
print(friends[3])
friends.insert(0,'Silvia')
print(friends)
friends.append('Isaac')
del friends[0]
print(friends)
popped_friend = friends.pop()
print(friends)
print(popped_friend)