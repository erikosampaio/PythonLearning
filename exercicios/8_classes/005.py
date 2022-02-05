# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes
# atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta=123, nome_correntista='Ériko', saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome_correntista = nome

    def deposito(self, deposito):
        if deposito <= 0:
            print('Valor inválido para depósito!')
        else:
            self.saldo += deposito
            print(f'Valor do depósito: R$ {deposito}')
            print(f'Saldo da conta após depósito: R$ {self.saldo}')

    def saque(self, saque):
        if saque <= 0:
            print('Valor inválido para saque!')
        elif (self.saldo - saque) < 0:
            print('Saldo insuficiente para saque!')
        else:
            self.saldo -= saque
            print(f'Valor do saque: R$ {saque}')
            print(f'Saldo da conta após saque: R$ {self.saldo}')


conta = ContaCorrente()

print(conta.numero_conta)
print(conta.nome_correntista)
print(conta.saldo)
print()

conta.alterar_nome('Jonatas')
print(conta.numero_conta)
conta.saque(20)
print()
conta.deposito(100)
print()
conta.saque(20)
print()
conta.saque(100)
