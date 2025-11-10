from conta import Conta
from banco import Banco

meu_banco = Banco('Inter') # Criei um objeto do tipo Banco, 1 banco pode ter várias contas
meu_banco.abrir_conta('leonardo',100) # Abri a conta
meu_banco.abrir_conta('Débora',6000) 
meu_banco.abrir_conta('teste', 100)
meu_banco.realizar_deposito(1,100)
meu_banco.realizar_deposito(2,100)
meu_banco.realizar_deposito(3,100)
meu_banco.realizar_saque(2,100) # Realizando saque da conta 2


