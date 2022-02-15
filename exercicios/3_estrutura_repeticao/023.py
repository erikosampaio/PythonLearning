"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

num = int(input("Informe um número: "))
execucoes = 0

for i in range(1, num+1):
    con = 0
    for n in range(1, num+1):
        execucoes += 1
        if i % n == 0:
            con += 1
    if con == 2:
        print(f'{i} é primo!')

print(f'Foram necessárias {execucoes} execuções para encontrar os números primos!')
