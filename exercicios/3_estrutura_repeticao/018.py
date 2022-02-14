"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

numero = 1
lista = []
while numero != 0:
    numero = int(input("Informe valores. Digite 0 para sair: "))
    if numero != 0:
        lista.append(numero)
    else:
        break

print(f'Lista: {lista}')
print(f'Menor número: {min(lista)}')
print(f'Maior número: {max(lista)}')
print(f'Soma dos valores: {sum(lista)}')
