# Faça um programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a cobertura
# da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
# latas de tinta a serem compradas e o preço total.

metros = float(input('Informe o tamano da área em metros quadrados: '))

litros = metros / 3
capacidade_lata = 18
preco_lata = 80
total_lata = litros / capacidade_lata

print(f'''
Metros quadrados: {metros:.2f} m²
Quantidade de tinta necessária para pintura: {litros:.2f} L
Quantidade de latas de tinta: {total_lata:.2f}
Valor Total: R$ {(preco_lata * total_lata):.2f}
''')
