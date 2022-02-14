"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numeros = []
for numero in range(5):
    numeros.append(int(input(f'Número {numero+1}/5: ')))

print(f'Números: {numeros}')
print(f'Soma dos números: {sum(numeros)}')
print(f'Média dos números: {(sum(numeros) / len(numeros)):.2f}')
