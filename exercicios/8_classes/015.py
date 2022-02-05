# Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de
# comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
# Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

class BichinhoVirtualPlus:
    def __init__(self, nome='Ériko', saude=5, fome=2, idade=1):
        self.nome = nome
        self.saude = saude
        self.fome = fome
        self.idade = idade

    def mostra_nome(self):
        return self.nome

    def mostra_saude(self):
        return self.saude

    def mostra_fome(self):
        return self.fome

    def mostra_idade(self):
        return self.idade

    def alterar_nome(self, nome):
        self.nome = nome

    def alterar_idade(self, idade):
        self.idade = idade

    def humor(self, diversao):
        self.saude -= diversao
        return self.saude

    def alterar_fome(self, comida):
        self.fome -= comida
        return self.fome


tamagushi = BichinhoVirtualPlus()

print(f'Nome: {tamagushi.mostra_nome()}')
print(f'Saúde: {tamagushi.mostra_saude()}')
print(f'Fome: {tamagushi.mostra_fome()}')
print(f'Idade: {tamagushi.mostra_idade()}')
print()


while True:
    try:
        print('Menu: Digite uma letra para sair!')
        print('\t1 -> Alterar nome: ')
        print('\t2 -> Alterar idade: ')
        print('\t3 -> Informar diversão: ')
        print('\t4 -> Informar comida: ')
        escolha = int(input('\tEscolha: '))
        if escolha == 1:
            nome = input("Informe o novo nome: ")
            tamagushi.alterar_nome(nome)
            print(f'Nome: {tamagushi.mostra_nome()}')
        elif escolha == 2:
            idade = int(input("Informe a nova idade: "))
            tamagushi.alterar_idade(idade)
            print(f'Idade: {tamagushi.mostra_idade()}')
        elif escolha == 3:
            diversao = int(input("Informe o valor da diversão: "))
            tamagushi.humor(diversao)
            print(f'Saúde: {tamagushi.mostra_saude()}')
        elif escolha == 4:
            comida = int(input("Informe o valor da comida: "))
            tamagushi.alterar_fome(comida)
            print(f'Fome: {tamagushi.mostra_fome()}')
        else:
            print('Informe um número válido!')
    except ValueError:
        print('Programa finalizado!')
        break

print(f'Nome: {tamagushi.mostra_nome()}')
print(f'Saúde: {tamagushi.mostra_saude()}')
print(f'Fome: {tamagushi.mostra_fome()}')
print(f'Idade: {tamagushi.mostra_idade()}')
print('Programa finalizado!')
