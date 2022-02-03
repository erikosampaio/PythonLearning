# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a == b and a == c:
    print('Os 3 números são iguais!')
else:
    maior = a
    menor = a
    if b > a and b > c:
        maior = b
    elif c > a and c > b:
        maior = c

    if b < a and b < c:
        menor = b
    elif c < a and c < b:
        menor = c

    print(f'Maior número: {maior}')
    print(f'Menor número: {menor}')

# Ou em Python:
print(f'Maior número: {max(a, b, c)}')
print(f'Menor número: {min(a, b, c)}')
