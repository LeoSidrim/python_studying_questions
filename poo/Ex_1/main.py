class Carro:
    def __init__(self, marca , modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro_1 = Carro('Ford', 'Ka', 2021)
carro_2 = Carro('Honda', 'Civic', 2023)


print(f'{carro_1.modelo}')
print(f'{carro_2.marca} {carro_2.ano}')

