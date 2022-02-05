# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
media = 0
for nota in range(4):
    notas.append(float(input(f'Informe a {nota+1}ª nota: ')))

media = sum(notas) / len(notas)

print()
for nota in range(len(notas)):
    print(f'{nota+1}ª nota: {notas[nota]}')

print()
print(f'Soma das notas: {sum(notas)}')
print(f'Média das notas: {media:.2f}')
