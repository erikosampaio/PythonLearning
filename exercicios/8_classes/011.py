# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#
# a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma
# certa quantidade de combustível no tanque.
# b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
# c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa
# distância, reduzindo o nível de combustível no tanque de gasolina.
# d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

# meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
# meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
# meuFusca.andar(100);            # anda 100 quilômetros.
# meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.

class Carro:
    def __init__(self, consumo, nivel=0):
        self.consumo = consumo
        self.nivel = nivel

    def andar(self, d):
        if self.nivel == 0:
            print('Tanque vazio. Abasteça')
        else:
            while d - self.consumo > 0 and self.nivel > 0:
                self.nivel -= 1
                d -= self.consumo
                if self.nivel == 1:
                    print(f'Você só tem mais {self.nivel} litro de combustível. Abasteça urgente!')
                elif self.nivel == 0:
                    print('Você ficou no prego de combustível')

    def adicionar_gasolina(self, adiciona):
        self.nivel += adiciona
        return f'Abastecido(s) {adiciona} litro(s) de combustível'

    def obter_gasolina(self):
        print(f'Você consumiu {abastece - self.nivel} litros.')
        return f'Restam {self.nivel} litro(s) no tanque.'


gol = Carro(int(input("Informe o consumo do seu veículo (km / l): ")))
distancia = int(input("Informe a distância a ser percorrida: "))
abastece = int(input("Informe quantos litros será abastecidos: "))

gol.adicionar_gasolina(abastece)
print()
gol.andar(distancia)
print()
print(gol.obter_gasolina())
