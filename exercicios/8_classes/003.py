# Classe Retangulo: Crie uma classe que modele um retangulo:

# a.Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b.Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# c.Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# d.Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, comprimento=None, altura=None):
        self.comprimento = comprimento
        self.altura = altura

    def mudar_valor(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

    def mostra_valor(self):
        return self.comprimento, self.altura

    def area(self):
        return self.comprimento * self.altura

    def perimetro(self):
        return (self.comprimento*2) + (self.altura * 2)


c = float(input("Informe o comprimento do retângulo: "))
a = float(input("Informe a altura do retângulo: "))

retangulo = Retangulo()

retangulo.altura = a
retangulo.comprimento = c

print(retangulo.mostra_valor())
retangulo.mudar_valor(4, 6)
print(retangulo.mostra_valor())
print(retangulo.area())
print(retangulo.perimetro())
