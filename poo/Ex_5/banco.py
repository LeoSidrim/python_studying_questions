from conta import Conta

class Banco:
    def __init__(self,nome):
        self.nome = nome
        self.contas = [] 

    def abrir_conta(self,titular,saldo_inicial):
        numero = len(self.contas) + 1
        conta = Conta (titular,numero,saldo_inicial)
        self.contas.append(conta)
        print(f'Conta [{numero}] aberta para [{titular}]')
    
    def buscar_conta(self, numero_conta):
        for i in self.contas: # i já é o próprio objeto, ele varre o array contas e assume a forma do objeto na determinada posição
            if i.numero_conta == numero_conta: #comparo o numero_conta do objeto com numero_conta parâmetro
                return i
            
        return None

    def realizar_deposito(self,numero_conta,valor_deposito):
        conta = self.buscar_conta(numero_conta) # armazeno objeto encontrado
        if conta: # Se conta existir deposita o valor
            conta.depositar(valor_deposito)
        else:
            print(f'Conta não encontrada')
            

    def realizar_saque(self,numero_conta,valor_saque):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.sacar(valor_saque)
        else:
            print(f'Conta não encontrada')

            


        
