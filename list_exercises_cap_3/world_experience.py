locals = ['Rio de Janeiro', 'Canada', 'São Paulo', 'Amazonas'] # Lista de locais aleatórios que eu gostaria de conhecer

print(locals)
print(sorted(locals)) # sorted ordena a lista de forma temporária, em ordem alfabética ou uma sequência numérica, não altera a lista originalmente
print(locals) # Lista permanece a mesma
locals.reverse() # Inverte a ordem atual permanentemente, o último vira o primeiro termo e assim por diante.
print(locals)
locals.reverse() # Reverti novamente, então voltou ao estado inicial
print(locals)
locals.sort() # Lista é ordenada alfabeticamente/numeral permanentemente
print(locals) 
locals.sort(reverse=True) # Altera a ordem de forma alfabética reversamente
print(locals)