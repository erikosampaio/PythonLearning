# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o
# número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do
# volume permanecem dentro de faixas válidas.

class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, canal):
        if canal <= 0 or canal > 60:
            print('Canal inválido!')
        else:
            self.canal = canal
            print(f'Você mudou para o canal {self.canal}')

    def aumentar_volume(self, aumentar):
        if aumentar < 0 or aumentar > 50:
            print('Volume inválido!')
        elif aumentar == 0:
            print('Você não aumentou o volume!')
        else:
            self.volume = aumentar
            print(f'Você aumentou para o volume {aumentar}')

    def diminuir_volume(self, diminuir):
        if diminuir < 0 or diminuir > 50:
            print('Volume inválido!')
        elif diminuir == 0:
            print('Você não aumentou o volume!')
        else:
            self.volume = diminuir
            print(f'Você diminuiu para o volume {diminuir}')


print('Quantidade de canais: 100')
print('Quantidade do volume: 50')

globo = Tv(10, 23)

print(globo.canal)
print(globo.volume)

globo.mudar_canal(7)
globo.aumentar_volume(30)

globo.mudar_canal(101)
globo.diminuir_volume(60)
globo.diminuir_volume(15)
