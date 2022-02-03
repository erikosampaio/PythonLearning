# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

num1 = int(input("Digite a primeira nota: "))
num2 = int(input("Digite a segunda nota: "))

media = (num1 + num2) / 2
print(f'Média = {media:.2f}')

if media == 10:
    print('Aprovado com Distinção!')
elif media >= 7:
    print('Aprovado!')
elif media < 7:
    print("Reprovado!")
