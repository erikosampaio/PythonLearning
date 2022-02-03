# Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor


circulo_primeiro = Bola()
circulo_segundo = Bola()

print(circulo_primeiro.mostra_cor())
print(circulo_segundo.mostra_cor())

circulo_segundo.troca_cor('Amarelo')
print(circulo_primeiro.mostra_cor())
print(circulo_segundo.mostra_cor())




