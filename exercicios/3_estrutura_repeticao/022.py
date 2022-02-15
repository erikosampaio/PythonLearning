"""
Altere o programa de cálculo dos números primos, informando, caso o número
não seja primo, por quais número ele é divisível.
"""

num = int(input("Informe um número: "))

con = 0
for i in range(1, num+1):
    if num % i == 0:
        con += 1

if con == 2:
    print(f'{num} é primo')
else:
    for i in range(1, num+1):
        if num % i == 0:
            print(f'{num} é divisível por {i}')
