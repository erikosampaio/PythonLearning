"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

while True:
    numero = int(input("Informe um número entre 1 e 10: "))
    if numero < 0 or numero > 10:
        pass
    else:
        for i in range(1, 11):
            print(f'{numero} x {i:2} = {numero * i:2}')
        break
