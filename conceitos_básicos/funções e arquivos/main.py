'''
Objetivo: Praticar a separação do código em arquivos (módulos). Este é o exercício mais importante.

Desafio (em duas partes):

Parte A: Criar o Módulo de "Utilidades"

    Crie um novo arquivo no seu projeto chamado calculos.py.

    Mova (copie e cole) a função calcular_media (do Exercício 2) para dentro deste novo arquivo calculos.py.

    No mesmo arquivo calculos.py, crie uma nova função chamada encontrar_maior que aceita três números e retorna o maior deles.

Parte B: Criar o Arquivo Principal

    Crie um segundo arquivo chamado main.py (ou use o seu arquivo principal).

    Dentro de main.py, você precisa importar as suas duas funções do arquivo calculos.py.

    No main.py, use a função calcular_media importada para calcular a média de 10, 20 e 30, e imprima o resultado.

    No main.py, use a função encontrar_maior importada para achar o maior entre 5, 100 e 20, e imprima o resultado.
'''

import functions

print(functions.calcular_media(10,20,30))
print(functions.encontrar_maior(100,100,100))