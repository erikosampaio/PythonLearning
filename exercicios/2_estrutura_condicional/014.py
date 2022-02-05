# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
# calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0            A
# Entre 7.5 e 9.0             B
# Entre 6.0 e 7.5             C
# Entre 4.0 e 6.0             D
# Entre 4.0 e zero            E
#
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
# for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2) / 2

if media < 0:
    print('Dados inválidos!')
else:
    print(f'Notas: {n1}, {n2}')
    print(f'Média: {media:.2f}')
    if 9 <= media <= 10:
        print('Conceito: ', end='')
        print('A')
        print('Aprovado')
    elif 7.5 <= media < 9:
        print('Conceito: ', end='')
        print('B')
        print('Aprovado')
    elif 6 <= media < 7.5:
        print('Conceito: ', end='')
        print('C')
        print('Aprovado')
    elif 4 <= media < 6:
        print('Conceito: ', end='')
        print('D')
        print('Reprovado')
    else:
        print('Conceito: ', end='')
        print('E')
        print('Reprovado')
