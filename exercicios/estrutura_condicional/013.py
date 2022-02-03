# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

n = int(input("Digite um número correspondente para o dia da semana: "))

if n <= 0 or n > 7:
    print('Valor inválido!')
else:
    if n == 1:
        print('Domingo.')
    elif n == 2:
        print('Segunda')
    elif n == 3:
        print('Terça')
    elif n == 4:
        print('Quarta')
    elif n == 5:
        print('Quinta')
    elif n == 6:
        print('Sexta')
    elif n == 7:
        print('Sábado')
