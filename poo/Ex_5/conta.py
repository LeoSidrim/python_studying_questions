class Conta:
    def __init__(self,titular,numero_conta,saldo_inicial):
        self.titular=titular
        self.numero_conta=int(numero_conta)
        self.saldo=float(saldo_inicial)

    def depositar(self,valor):
        self.saldo += valor
        return print(f'Novo saldo: R${self.saldo}')
    
    def sacar(self,valor_saque):
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            return print(f'Novo saldo: R${self.saldo}')
        else:
            return print(f'Saldo insuficiente')
        
    def ver_saldo(self):
        return print(f'Saldo atual: R$ {self.saldo}')
    
    