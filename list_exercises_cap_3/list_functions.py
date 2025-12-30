programming_languages = ['python', 'java', 'ruby', 'cobol', 'javascript', 'rust']  # Lista com nomes de linguagens de programação
programming_languages.append('C++') # Adiciono elemento no final da lista 
var = programming_languages.pop() # Removo o último elemento e armazeno na variável temporária
print(f'Eu já programei em {var}') # Printo a mensagem com a variável
programming_languages.remove('python') # Remove primeira ocorrencia do item da lista
del programming_languages[2] # Remove pelo índice
programming_languages.insert(0,'C') # Adiciona o valor no índice desejado.
print(sorted(programming_languages)) # Ordena temporariamente
programming_languages.reverse() # reverte ordem da lista
programming_languages.reverse() # reverte novamente a ordem
programming_languages.sort() # Ordena permanentemente 
programming_languages.sort(reverse=True)
print(programming_languages)
print(f'Total de linguagens que já ouvi falar {len(programming_languages)}')

increasing_numbers = []
for number in range(1,11): # Função range() para entregar uma sequência de números.
    increasing_numbers.append(number)
print(f'Lista dos 10 primeiros números em ordem crescente {increasing_numbers}')

decreasing_numbers = []
for number in range(10,0,-1): # Primeiro sempre incluido, último sempre excluído.
    decreasing_numbers.append(number)
print(f'Lista dos 10 primeiros números em ordem decrescente {decreasing_numbers}')


squares = []
for square in range(1,11): # Lista de 10 números (Vai repetir 10 vezes)
    squares.append(square**2) #  square elevado ao quadrado vai ser inserido na lista squares 
print(f'Lista dos primeiros 10 números quadrados {squares}')

list = [1,2,3,45,3213,532,545124,23122,32]
print(max(list)) # Pega o maior elemento de uma Lista (Posso usar para mostrar quem tem mais pontos no leaderboard)
print(min(list)) # Pega o menor elemento de uma Lista
print(sum(list)) # Soma todos os elementos de uma lista