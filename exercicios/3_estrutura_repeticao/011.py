"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
soma = 0

if num1 == num2:
    print('Números iguais')
elif max(num1, num2) - min(num1, num2) == 1:
    print('Não existe números inteiros entre os dois números')
else:
    for numero in range(min(num1, num2)+1, max(num1, num2)):
        print(numero)
        soma += numero

print()
print(soma)
