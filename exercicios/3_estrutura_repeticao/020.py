"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
limitando o fatorial a números inteiros positivos e menores que 16.
"""

num = 1
while True:
    num = int(input("Digite o número de 1 a 15 para fatorial. Digite 0 ou número negativo para sair: "))
    if num <= 0:
        print('Fim do programa!')
        break
    else:
        if 0 < num < 16:
            aux = num
            fatorial = aux
            while aux > 1:
                fatorial *= (aux-1)
                aux -= 1
            print(f'Fatorial de {num} = {fatorial}')
        else:
            print('Informe um valor entre 1 e 16!')
