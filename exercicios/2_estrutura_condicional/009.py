# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 == n2 and n1 == n3:
    print('Números iguais!')
else:
    primeiro = n1
    segundo = n1
    terceiro = n1
    if n2 < n1 and n2 < n3:
        primeiro = n2
        if n1 < n3:
            segundo = n1
            terceiro = n3
        else:
            segundo = n3
            terceiro = n1

    elif n3 < n1 and n3 < n2:
        primeiro = n3
        if n1 < n2:
            segundo = n1
            terceiro = n2
        else:
            segundo = n2
            terceiro = n1

    else:
        if n2 < n3:
            segundo = n2
            terceiro = n3
        else:
            segundo = n3
            terceiro = n2

    print(primeiro, segundo, terceiro)
