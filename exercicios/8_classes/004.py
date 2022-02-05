# Classe Pessoa: Crie uma classe que modele uma pessoa:
#
# a.Atributos: nome, idade, peso e altura
# b.Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self, engordou):
        self.peso += engordou

    def emagrecer(self, emagreceu):
        self.peso -= emagreceu


eriko = Pessoa('Ériko', 2, 12, 80)

print(f'O {eriko.nome} tem {eriko.idade} anos e pesa {eriko.peso} Kg.\n')
for _ in range(22):
    eriko.envelhecer()
    print(f'Agora o {eriko.nome} tem {eriko.idade:2} anos.'
          f'Sua altura é de {eriko.altura} cm.')
print()

eriko.engordar(70)
print(f'Atualmente, o {eriko.nome} tem {eriko.idade} anos.')
print(f'Engordou e passou a ter {eriko.peso} Kg.')
eriko.emagrecer(5)
print(f'Após isso, emagreceu, e ficou com {eriko.peso} Kg.')
