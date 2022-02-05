# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista.
# Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário tome conta de um único bichinho, exija
# que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para
# todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
# Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
import random

class Bichinhos:
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


b1 = Bichinhos('Dora', random.randint(1, 10), random.randint(1, 10), 2)
b2 = Bichinhos('Yoshi', random.randint(1, 10), random.randint(1, 10), 2)
b3 = Bichinhos('Briochy', random.randint(1, 10), random.randint(1, 10), 2)
b4 = Bichinhos('Nilo', random.randint(1, 10), random.randint(1, 10), 2)

lista = [b1, b2, b3, b4]
y = 1
for i in lista:
    print(f'Nome do b{y}: {i.mostra_nome()}')
    print(f'Saúde do b{y}: {i.mostra_saude()}')
    print(f'Fome do b{y}: {i.mostra_fome()}')
    print(f'Idade do b{y}: {i.mostra_idade()}')
    y += 1
    print()

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
            y = 1
            for i in lista:
                i.alterar_nome(input(f'Informe o novo nome do b{y}: '))
                y += 1
        elif escolha == 2:
            y = 1
            for i in lista:
                i.alterar_saude(input(f'Informe a saúde do b{y}: '))
                y += 1
        elif escolha == 3:
            y = 1
            for i in lista:
                i.alterar_fome(input(f'Informe a fome do b{y}: '))
                y += 1
        elif escolha == 4:
            y = 1
            for i in lista:
                i.alterar_idade(input(f'Informe a nova idade b{y}: '))
                y += 1
        else:
            print('Informe um valor válido!')
    except ValueError:
        break

print()
y = 1
for i in lista:
    print(f'Nome do b{y}: {i.mostra_nome()}')
    print(f'Saúde do b{y}: {i.mostra_saude()}')
    print(f'Fome do b{y}: {i.mostra_fome()}')
    print(f'Idade do b{y}: {i.mostra_idade()}')
    y += 1
    print()
