# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente
# o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
#   harry=funcionário("Harry",25000)
#   harry.aumentarSalario(10)

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def mostra_nome(self):
        return self.nome

    def mostra_salario(self):
        return self.salario

    def aumenta_salario(self, taxa):
        self.salario += (self.salario * (taxa / 100))
        return self.salario


eriko = Funcionario('Eriko', 1300)

print(eriko.mostra_nome())
print(eriko.mostra_salario())
eriko.aumenta_salario(10)
print(f'{eriko.mostra_salario():,.2f}')
