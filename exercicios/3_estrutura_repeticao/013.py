"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

base = int(input("Base: "))
expoente = int(input("Expoente: "))
resultado = 1

for i in range(expoente):
    resultado = resultado * base


print(resultado)
