# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 == n2 and n2 == n3:
    print('Os 3 números são iguais')
elif n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)
