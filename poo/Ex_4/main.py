'''
Desafio:

    Crie uma classe Carro.

    No __init__, ele deve receber marca e modelo.

    O __init__ também deve definir dois atributos de estado interno, sempre começando com os mesmos valores:

        self.ligado = False

        self.velocidade = 0

    Crie um método ligar().

        Ele só deve funcionar se o carro estiver desligado (if self.ligado == False:).

        Se funcionar, deve mudar self.ligado para True e imprimir "Carro ligado!".

        Se o carro já estiver ligado, deve apenas imprimir "O carro já está ligado."

    Crie um método desligar().

        Só deve funcionar se o carro estiver ligado.

        Deve mudar self.ligado para False e self.velocidade para 0 (não se pode desligar um carro em movimento!).

        Deve imprimir "Carro desligado."

    Crie um método acelerar(valor).

        Ele só deve funcionar se o carro estiver ligado.

        Se estiver ligado, deve aumentar self.velocidade pelo valor recebido e imprimir a nova velocidade (ex: "Vrum! Velocidade: 20 km/h").

        Se estiver desligado, deve imprimir "Ligue o carro primeiro!".

    Crie um método frear(valor).

        Deve diminuir self.velocidade pelo valor, mas nunca deixar a velocidade ficar negativa (ela deve parar em 0).

        Deve imprimir a nova velocidade.

Teste seu código: Crie um Carro (ex: meu_fusca), tente acelerar com ele desligado, ligue-o, acelere duas vezes, freie uma vez e, por fim, desligue-o.
'''

class Carro:
    def __init__ (self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print('Carro já está ligado')
        else:
            self.ligado = True
            print('Carro ligado!')

    def desligar(self):
        if self.ligado and self.velocidade == 0: 
            self.ligado = False
            print('Carro desligado')
        elif self.ligado == True and self.velocidade != 0:
            print('Não se pode desligar um carro em movimento!')
        else:
            print('Carro já está desligado')
    
    def acelerar(self,valor):
        if self.ligado:
            self.velocidade += valor
            print(f'Vrum! Velocidade:{self.velocidade} km/h')
        else:
            print('Ligue o carro primeiro!')

    def frear(self,valor):
        if self.velocidade > 0:
            self.velocidade -= valor 
            if self.velocidade < 0:
                self.velocidade = 0
                print('O carro parou.')
            else:
                print(f'Velocidade: {self.velocidade} km/h')
        else:
            print('Veículo já esta parado.')

meu_fusca = Carro('Vollkswagem','Fusca')
meu_fusca.acelerar(10)
meu_fusca.ligar()
meu_fusca.acelerar(10)
meu_fusca.acelerar(10)
meu_fusca.frear(10)
meu_fusca.frear(20)
meu_fusca.desligar()
