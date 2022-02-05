# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando
# as seguintes fórmulas:

# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input("Informe a altura: "))
peso_ideal_homem = 72.7 * h - 58
peso_ideal_mulher = 62.1 * h - 44.7

print(f'Se você for homem, seu peso ideal é: {peso_ideal_homem:.2f} Kg')
print(f'Se você for mulher, seu peso ideal é: {peso_ideal_mulher:.2f} Kg')
