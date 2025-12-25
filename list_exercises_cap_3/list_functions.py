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


