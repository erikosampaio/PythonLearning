# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com
# a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial
# como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
# Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:
    def __init__(self, numero=123, nome_correntista='Ériko', saldo: float = 1000, taxa: float = 10):
        self.numero = numero
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        self.taxa = taxa

    def adicione_juros(self):
        self.saldo += (self.saldo / self.taxa)
        return f'{self.saldo:,.2f}'


conta = ContaInvestimento()

print(f'Nome do correntista: {conta.nome_correntista}')
print(f'Número da conta: {conta.numero}')
print(f'Saldo inicial: R$ {conta.saldo:,.2f}')
print(f'Taxa mensal: R$ {conta.taxa}%')

for i in range(5):
    print(f'\tSaldo no {i+1}º mês: {conta.adicione_juros()}')

print(f'Saldo final: R$ {conta.saldo}')
