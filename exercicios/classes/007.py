# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# a. Atributos: Nome, Fome, Saúde e Idade
# b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde Idade

# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor
# é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um
# atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self, nome, saude, fome, idade):
        self.nome = nome
        self.saude = saude
        self.fome = fome
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_saude(self, saude):
        self.saude = saude

    def alterar_fome(self, fome):
        self.fome = fome

    def alterar_idade(self, idade):
        self.idade = idade

    def mostra_nome(self):
        return self.nome

    def mostra_saude(self):
        return self.saude

    def mostra_fome(self):
        return self.fome

    def mostra_idade(self):
        return self.idade

    def humor(self):
        if self.saude <= 0:
            return f'Seu baby está doente!'
        elif self.saude - self.fome <= 0:
            return f'Seu baby está com fome!'
        return f'Seu baby está bem!'


tamagushi = BichinhoVirtual('Yoshi', 0, 10, 2)

print(f'Nome: {tamagushi.nome}')
print(f'Saúde: {tamagushi.saude}')
print(f'Fome: {tamagushi.fome}')
print(f'Idade: {tamagushi.idade}')
print(tamagushi.humor())

tamagushi.alterar_nome('Izzy')
tamagushi.alterar_saude(5)
tamagushi.alterar_fome(7)
tamagushi.alterar_idade(3)

print(f'Nome: {tamagushi.nome}')
print(f'Saúde: {tamagushi.saude}')
print(f'Fome: {tamagushi.fome}')
print(f'Idade: {tamagushi.idade}')
print(tamagushi.humor())
