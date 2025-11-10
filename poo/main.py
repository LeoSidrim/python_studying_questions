class Carro:
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Corolla','Azul',2025)

print(carro1.modelo)