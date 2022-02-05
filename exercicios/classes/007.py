# Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

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


tamagushi = BichinhoVirtual('Yoshi', 5, 2, 1)
print(f'Nome: {tamagushi.mostra_nome()}')
print(f'Saúde: {tamagushi.mostra_saude()}')
print(f'Fome: {tamagushi.mostra_fome()}')
print(f'Idade: {tamagushi.mostra_idade()}')
print()

print('Menu: Digite uma letra para sair!')
while True:
    try:
        print('\t1 -> Alterar nome: ')
        print('\t2 -> Alterar saúde: ')
        print('\t3 -> Alterar fome: ')
        print('\t4 -> Alterar idade: ')
        escolha = int(input('\tEscolha: '))
        if escolha == 1:
            nome = input("Informe o novo nome: ")
            tamagushi.alterar_nome(nome)
            print(f'Nome: {tamagushi.mostra_nome()}\n')
        elif escolha == 2:
            saude = int(input("Informe o valor da saude: "))
            tamagushi.alterar_saude(saude)
            print(f'Saúde: {tamagushi.mostra_saude()}\n')
        elif escolha == 3:
            fome = int(input("Informe o valor da fome: "))
            tamagushi.alterar_fome(fome)
            print(f'Fome: {tamagushi.mostra_fome()}\n')
        elif escolha == 4:
            idade = int(input("Informe o valor da idade: "))
            tamagushi.alterar_idade(idade)
            print(f'Idade: {tamagushi.mostra_idade()}\n')
        else:
            print('Informe um número válido!')
            print()
    except ValueError:
        break

print()
print(f'Nome: {tamagushi.mostra_nome()}')
print(f'Saúde: {tamagushi.mostra_saude()}')
print(f'Fome: {tamagushi.mostra_fome()}')
print(f'Idade: {tamagushi.mostra_idade()}')
print('Programa finalizado!')