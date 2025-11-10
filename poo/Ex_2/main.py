'''
Exercício: O Catálogo de Produtos

Objetivo: Reforçar o conceito e praticar a modificação de um atributo depois que o objeto foi criado.

Desafio:

    Crie uma classe chamada Produto.

    O construtor deve receber três argumentos: nome, preco e categoria.

    Armazene-os como atributos.

    Crie um objeto produto_1 que seja um "Notebook", com preço 5000 e categoria "Tecnologia".

    Imprima o nome e o preco do produto_1.

    Houve uma promoção! Altere o atributo preco do produto_1 para 4500 (faça isso fora da classe, simplesmente modificando o atributo do objeto).

    Imprima o novo preco do produto_1 para confirmar a alteração.
'''

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

produto_1 = Produto('Notebook', 5000, 'Tecnologia')

print(f'{produto_1.nome} {produto_1.preco}')
produto_1.preco = 4500
print(f'{produto_1.preco}')
