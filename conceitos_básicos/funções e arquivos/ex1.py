'''
3. Exercício de Função com Lógica: O Verificador de Idade

Objetivo: Combinar funções, parâmetros, return e if/else.

Desafio:

    Crie uma função chamada verificar_maioridade.

    A função deve aceitar um parâmetro: idade.

    Dentro da função:

        Se a idade for maior ou igual a 18, a função deve retornar o booleano True.

        Caso contrário, a função deve retornar o booleano False.

    Fora da função:

        Peça ao usuário para digitar sua idade (input).

        Chame a função verificar_maioridade passando a idade do usuário.

        Use o resultado (True ou False
'''


def verificar_maioridade(idade):
    return True if idade >= 18 else False

idade = int(input('Digite sua idade: '))

if verificar_maioridade(idade) == True:
    print('Acesso permitido')
else:
    print('Acesso negado')
    