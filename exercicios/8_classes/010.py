# Classe Bomba de Combustível: Faça um programa completo utilizando 8_classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# tipoCombustivel.
# valorLitro
# quantidadeCombustivel
# Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipoC, valorL, qtdC):
        self.tipoC = tipoC
        self.valorL = valorL
        self.qtdC = qtdC

    def abastecer_por_valor(self, valor):
        litros = valor / self.valorL
        self._apresentar_abastecimento_se_possivel(litros, valor)

    def _apresentar_abastecimento_se_possivel(self, litros, valor):
        if self.qtdC >= litros:
            self.qtdC -= litros
            print(f'Litros Abastecidos: {litros:.2f} L'
                  f'\nValor: R$ {valor:.2f}'
                  f'\nA bomba ainda possui {self.qtdC:.2f} L\n')
        else:
            print(f'Bomba vazia. Faltam {(litros - self.qtdC):.2f} L'
                  f'\nReabasteça a Bomba!')

    def abastecer_por_litro(self, litros):
        valor = litros * self.valorL
        self._apresentar_abastecimento_se_possivel(litros, valor)

    def alterar_valor(self, valor):
        self.valorL = valor

    def adicionar_combustivel(self, qtd):
        if qtd >= 0:
            self.qtdC += qtd
            print(f'Adicionado {qtd} Litros na bomba')
        else:
            print('Malandrinho, você não vai roubar combustível dessa bomba!')


bomba = BombaCombustivel('Gasolina', 4.59, 100)

bomba.abastecer_por_valor(100)
bomba.abastecer_por_litro(50)

bomba.alterar_valor(5.59)
bomba.abastecer_por_litro(50)  # Bomba ficou vazia, por ter apenas 28.21 L.
print()
bomba.adicionar_combustivel(100)
print()
bomba.abastecer_por_litro(50)

bomba.adicionar_combustivel(-100)
