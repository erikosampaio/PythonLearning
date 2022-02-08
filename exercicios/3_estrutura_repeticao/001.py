# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
        nota = int(input("Informe uma nota de 0 a 10: "))
        if 0 < nota <= 10:
            break
        else:
            print('Valor inválido!')
    except ValueError:
        print('Válido apenas números!')
