# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos
# os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos
# dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada
# refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome: str, estomago: list):
        self.nome = nome
        self.estomago = estomago

    def comer(self, comida):
        self.estomago.append(comida)
        print(self.estomago)

    def ver_bucho(self):
        return self.estomago

    def digerir(self):
        pass


m1 = Macaco('Donkey', [])
m2 = Macaco('Donkey', [])

for i in range(3):
    m1.comer(input(f"{i+1}º Alimento Macaco 1: "))
    m2.comer(input(f"{i + 1}º Alimento Macaco 2: "))

m1.comer(m2)  # É possível
