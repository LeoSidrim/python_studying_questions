'''
Exercício: O Perfil de Usuário

Objetivo: Combinar o que você aprendeu com diferentes tipos de dados (strings, números, booleanos).

Desafio:

    Crie uma classe chamada Usuario.

    O construtor deve receber nome_completo, email e idade.

    Além desses, o construtor também deve definir um atributo padrão chamado esta_ativo, que deve sempre começar com o valor True (não precisa ser um parâmetro).

    Crie um objeto usuario_leo com seus dados.

    Crie um objeto usuario_ana com dados fictícios.

    Imprima o email do usuario_leo.

    Imprima o nome_completo e a idade da usuario_ana.

    Imprima o status esta_ativo de ambos os usuários (deve ser True para os dois).
'''

class Usuario:
    def __init__ (self, nome_completo, email, idade):
        self.nome_completo = nome_completo
        self.email = email
        self.idade = idade
        self.esta_ativo = True # Posso criar sem passar o parâmetro

usuario_leo = Usuario('Leonardo Henrique Silva Sidrim', 'l.sidrim.dev@proton.me', 20)
usuario_ana = Usuario('Ana barroso gomes costa', 'ana@gmail.com', 23)

print(f'{usuario_ana.nome_completo} {usuario_ana.idade}')
print(f'{usuario_ana.esta_ativo}')
print(f'{usuario_leo.esta_ativo}')