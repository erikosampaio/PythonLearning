"""
Faça um programa que leia 5 números e informe o maior número.
"""

numeros = [0] * 5
maior = numeros[0]
for numero in range(5):
    numeros[numero] = (int(input(f"Número {numero+1}/5: ")))
    if numeros[numero] > maior:
        maior = numeros[numero]

print(f'Números: {numeros}')
print(f'Maior: {maior}')
