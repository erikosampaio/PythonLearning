"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

lista = []
numero = 1

while True:
    numero = int(input("Informe a idade da pessoa. Digite 0 para sair: "))
    if numero <= 0:
        break
    else:
        lista.append(numero)

media = sum(lista) / len(lista)

if 0 <= media <= 25:
    print(f'A turma é jovem. Média de idade = {media}')
elif 26 <= media <= 60:
    print(f'A turma é adulta. Média de idade = {media}')
else:
    print(f'A turma é idosa. Média de idade = {media:.2f}')
