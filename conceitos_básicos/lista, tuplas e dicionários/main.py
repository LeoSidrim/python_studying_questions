# criar uma função para cadastrar alunos

turma = [] # Criei uma lista chamada 'turma'



def cadastro_aluno(codigo,nome,idade,curso): # Declarei a função 'cadastro_aluno'
  aluno= {} # 'Cada vez que a função roda cria um dicionário 'aluno' 
  aluno['codigo'] = codigo
  aluno['nome'] = nome        # Insere os dados dos alunos 
  aluno['idade'] = idade
  aluno['curso'] = curso
  turma.append(aluno) # Insere o dicionário aluno na lista

print('---Sistema de cadastro---')

while True:
  codigo = int(input('Digite código do aluno (Necessita ser um número inteiro): '))
  nome = input('Digite seu nome: ')
  idade = int(input('Digite sua idade: '))
  curso = input('Digite seu curso: ')
  cadastro_aluno(codigo, nome, idade, curso) # Passo os dados que o usuário digitou e chamo a função
  

  resposta = input('Deseja continuar cadastrando? (sim/não) ') 
  
  if resposta.lower() == 'não': # Usei .lower() para garatir que vai sair 'não'
    break

print('Lista dos alunos:\n ')
for index, item in enumerate(turma,1): # Função enumerate para facilitar, recebe a lista o first number e varre a lista inteira.
  print(f"Aluno: {index}\n Codigo: {item['codigo']}\n Nome: {item['nome']}\n Idade: {item['idade']}\n Curso: {item['curso']}\n")
''