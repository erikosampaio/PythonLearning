"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

num = int(input("Informe um número: "))

con = 0
for i in range(1, num+1):  # Para cada número até número
    if num % i == 0:
        con += 1

if con == 2:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')
