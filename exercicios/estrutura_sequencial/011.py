# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo.
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num_real = float(input("Número real: "))

produto_dobro_do_primeiro_pela_metade_do_segundo = (num1 * 2) * (num2 / 2)
soma_triplo_primeiro_com_terceiro = (num1 * 3) + num_real
num_real_elevado_tres = num_real ** 3

print(f'O produto do dobro do primeiro com metade do segundo = '
'{produto_dobro_do_primeiro_pela_metade_do_segundo:.2f}')
print(f'A soma do triplo do primeiro com o terceiro = '
'{soma_triplo_primeiro_com_terceiro:.2f}')
print(f'O terceiro elevado ao cubo = {num_real_elevado_tres:.2f}')
