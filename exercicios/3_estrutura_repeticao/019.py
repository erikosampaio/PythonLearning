"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

numero = 1
lista = []
while True:
    try:
        numero = int(input("Informe valores entre 0 e 1000. Digite um caractere para sair: "))
        if 0 <= numero < 1001:
            lista.append(numero)
        else:
            print('Valor tem que está entre 0 e 1000!')
    except ValueError:
        break

print(f'Lista: {lista}')
print(f'Menor número: {min(lista)}')
print(f'Maior número: {max(lista)}')
print(f'Soma dos valores: {sum(lista)}')
