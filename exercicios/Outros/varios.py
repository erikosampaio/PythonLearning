"""
saque = int(input("Valor do saque: "))
um = saque

cem, um = divmod(um, 100)
cinquenta, um = divmod(um, 50)
dez, um = divmod(um, 10)
cinco, um = divmod(um, 5)


print(f'Valor do saque: {saque}')

if cem > 0:
    print(f'{cem} nota(s) de 100.')
if cinquenta > 0:
    print(f'{cinquenta} nota(s) de 50.')
if dez > 0:
    print(f'{dez} nota(s) de 10.')
if cinco > 0:
    print(f'{cinco} nota(s) de 5.')
if um > 0:
    print(f'{um} nota(s) de 1.')
"""
from random import random

"""
while True:
    try:
        numero = int(input("Informe um número de 0 a 10: "))
    except ValueError:
        print('Deve ser fornecido um valor inteiro.')
        print('Passei pelo except não sendo um valor inteiro.\n'.upper())
    else:
        if 0 <= numero <= 10:
            print(f'Número informado é: {numero}')
            print('Não passei pelo ValueError.'.upper())
            print('Passei pelo 1º else sendo um número entre 0 e 10.\n'.upper())
            break
        else:
            print('O número informado deve estar entre 0 e 10!')
            print('Não passei pelo ValueError.'.upper())
            print('Passei pelo 2º else não sendo um número entre 0 e 10.\n'.upper())
"""

"""
maximo = int(input("Número: "))

for _ in range(4):
    maximo = max(maximo, int(input("Número: ")))
    print(f'Maior número até agora: {maximo}')

print(f'\nMaior número digitado: {maximo}')
"""

"""
soma = float(input("Número: "))
media = 0

for n in range(2, 6):
    soma += float(input("Número: "))
    media = soma / n
    print(f'A soma dos números é: {soma}, e a média é: {media}')
"""

"""
lista = []
qtd = 0

print('Informe valores, sendo um número inferior a -1 para parar.')
while True:
    num = float(input("Número: "))
    qtd += 1
    if num < -1:
        break
    lista.append(float(num))


print(f'\nQuantidade de valores lidos: {qtd}')
print(f'\nValores da lista um ao lado do outro na ordem em que foram informados:')
print(' '.join(str(nota) for nota in lista))
print(f'\n\nValores da lista na ordem inversa um abaixo do outro:')
for valor in range(len(lista)-1, -1, -1):
    print(lista[valor])
print(f'\nSoma da lista: {sum(lista)}')
print(f'\nMédia da lista: {sum(lista) / len(lista):.2f}')
print(f'\nValores que estão acima da média da lista: ')
print(' '.join([str(nota) for nota in lista if nota > (sum(lista) / len(lista))]))
qtd_menor_7 = 0
for valor in lista:
    if valor < 7:
        qtd_menor_7 += 1
print(f'\nQuantidade de valores da lista abaixo de 7: {qtd_menor_7}')
print('\nPrograma finalizado com Sucesso!')
"""

"""
salarios = [345, 456, 788, 234, 7896, 234, 34234, 787, 890, 987, 231]
faixa_salarial = [0] * 9

for salario in salarios:
    indice = salario // 100 - 2
    indice_maximo = len(faixa_salarial) - 1
    indice = min(indice, indice_maximo)
    faixa_salarial[indice] += 1

faixa = 200
for qtd in faixa_salarial:
    print(f'{qtd} salários na faixa {faixa}')
    faixa += 100
"""

"""
def ate_numero(n):
    for i in range(1, n+1):
        for _ in range(i):
            print(i, end='   ')
        print()
    return 'ok'


num = int(input("Numero: "))

print(ate_numero(num))
"""

"""
def ate_numero(n):
    for i in range(1, n+1):
        for x in range(1, i+1):
            print(x, end='   ')
        print()
    return 'ok'


num = int(input("Numero: "))

print(ate_numero(num))
"""

"""
str1 = input('1ª: ')
str2 = input('2ª: ')


print(str1)
print(str2)

print(len(str1))
print(len(str2))

if len(str1) == len(str2):
    print('Strings com mesmo tamanho!')
else:
    print('Strings com tamanhos diferentes!')


if str1 == str2:
    print('Strings com mesmo conteúdo!')
else:
    print('Strings com conteúdos diferentes!')
"""

"""
nome = input('nome: ').upper()
nome_invertido_letra = ''.join(reversed(nome))
nome_invertido_palavra = ' '.join(reversed(nome.split(' ')))

print(nome)
print(nome_invertido_letra)
print(nome_invertido_palavra)
"""

"""
A = 80_000
B = 200_000
anos = 0

while True:
    # print(f'População no {anos + 1}º ano: ')
    # print(f'População A: {int(A)}')
    # print(f'População B: {int(B)}\n')
    A *= 1.03
    B *= 1.015
    A = int(A)
    B = int(B)
    anos += 1
    if A == B:
        # print(f'População no último ano: ')
        print(f'\033[36mPopulação no ano {anos}:\033[m ')
        print(f'\033[33mA: {int(A)}.\033[m')
        print(f'\033[32mB: {int(B)}.\033[m')
        break
    elif A > B:
        print(f'\033[36mPopulação no ano {anos}:\033[m ')
        print(f'\033[33mA: {int(A)}.\033[m')
        print(f'\033[32mB: {int(B)}.\033[m')
        print(f'\033[34mDiferença de habitantes:\033[m \033[31m{int(A - B)}\033[m.''')
        break
"""

"""

import random

palavras = ['azul', 'nayara', 'ceu', 'trabalho', 'amor', 'armario', 'deus']
escolha = palavras[random.randint(0, len(palavras))]

print('A palavra é: ', end='')
for letra in escolha:
    print(f'_ ', end='')

conjunto_letras_escolha = set(escolha)
conjunto_letras_digitadas = set()
erros = 0

while (not conjunto_letras_escolha.issubset(conjunto_letras_digitadas)) and erros < 7:
    print()
    letra = input("Digite uma letra: ").lower()
    conjunto_letras_digitadas.add(letra)
    if letra in conjunto_letras_escolha:
        print('A palavra é: ', end='')
        for letra in escolha:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print('_ ', end='')
    else:
        erros += 1
        print(f'Erro -> {erros} de 6. Tente de novo!')
    print()
    print('Letras já digitadas: ', conjunto_letras_digitadas)

print()
if erros < 7:
    print('Parabéns, você ganhou!')

else:
    print('Infelizmente você perdeu!')
print(f'A palavra digitada é: {escolha}'.upper())

"""

"""
print(linguas['br'])
print(linguas['eua'])
# print(linguas['es'])  # Error. Não existe essa chave
print(linguas.get('es', 'Língua não definida!'))
print(linguas.get('br'))
print('eua' in linguas)

print(6 in list(range(10)))
print(12 in list(range(10)))

linguas['es'] = 'espanhol'
print(linguas['es'])
linguas['fce'] = 'frances'
print(linguas['fce'])
linguas['es'] = 'amor'
print(linguas['es'])
"""

"""
linguas = {'br': 'portugues', 'eua': 'ingles'}
linguas['es'] = 'espanhol'
linguas['fce'] = 'frances'

for valor in linguas.items():
    print(valor)

print()
fce = linguas.pop('fce')
print(f'{fce} --> Valor removido e retornado em uma variável.')
print(linguas)

del linguas['br']  # Valor apenas deletado do dicionário

print()
print(linguas)
"""

"""
def ola(nome):
    return f'Olá {nome}!'


print(ola('Ériko'))


def ola1(nome, sobrenome):
    return f'Olá {nome} {sobrenome}!'


print(ola1('Ériko', 'Sampaio'))


def ola3(nome, sobrenome='Sampaio'):
    return f'Olá {nome} {sobrenome}'


print(ola3('Ériko', 'dos Santos'))


def ola3(nome, sobrenome='Sampaio', idade=28):
    return f'Olá {nome} {sobrenome} {idade}'


print(ola3('Ériko', 'dos Santos'))
print(ola3(sobrenome='Ériko', nome='Sampaio', idade=54))
"""

"""
def arg(*args):
    print(args)
    print(type(args))


arg(2, 3, 4)


def soma(*args):
    aux = 0
    for i in args:
        aux += i
    return aux


print(soma(2, 4, 5))


def kwargs(**kwargs):
    return kwargs


print(kwargs(nome='amor', sobrenome='paixão'))
"""

"""
from exercicios import contagem_de_caracteres_lista
from exercicios import contagem_de_caracteres_dic

lista = ['Eriko', 'Nayara', 'Valdecio', 'Marta', 'Paula', 'Tarciane']

for nome in range(len(lista)):
    lista[nome] = lista[nome].lower()

for nome in lista:
    print(contagem_de_caracteres_dic.contar_caracteres(nome))
    print()
"""

"""
nome = 'nayara'
dic = {}

for caracter in nome:
    dic[caracter] = dic.get(caracter, 0) + 1

print(dic)
"""

"""
nome = 'nayara'
dic = {}

for caracter in nome:
    dic[caracter] = dic.get(caracter, 0) + 1

print(dic)

for letra in range(len(nome) + 1):
    print(nome[:letra])  # Imprime nome progresivamente

for letra in range(len(nome), -1, -1):
    print(nome[:letra:])  # Imprime nome regressivamente

while nome != '':
    print(nome)
    nome = nome[:-1]   # Imprime nome regressivamente
"""


