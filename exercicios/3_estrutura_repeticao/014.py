"""
Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares.
"""

numeros = []
pares = []
impares = []

for numero in range(10):
    numeros.append(int(input(f"Número {numero + 1}/10: ")))
    if numeros[numero] % 2 == 0:
        pares.append(numeros[numero])
    else:
        impares.append(numeros[numero])

print(f'Números: {numeros}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
