books = ['genesis','Exodus','Leviticus','Numbers', 'romanos'] # Para criar uma lista utilize [] (colchetes) 

# Uma lista é um coleção ordenada, ou seja, podemos acessar cada elemento de uma lista se tivermos um índice.

print(books) # Quando printamos uma lista sem especificar o elemento, a lista inteira é exibida. Inclusive com os []
print(books[0]) # Para especificar o item utilizamos os [index], nome da variável[index]list
print(books[0].title()) # Posso utilizar uma função para formatar a saída do item
print(books[-1]) # Posso utilizar valores negativos para acessar os últimos valores de uma lista.

message = f"Meu livro favorito da bíblia é {books[-1].title()}" 
print(message)