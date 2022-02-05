# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

while True:
    try:
        valor = int(input("Informe um valor: "))
        break
    except ValueError:
        print('Informe um valor inteiro!')

if valor == 0:
    print('Valor Neutro (0)')
elif valor >= 1:
    print('Positivo')
else:
    print('Negativo!')
