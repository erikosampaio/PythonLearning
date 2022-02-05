# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de
# 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem
# compradas e os respectivos preços em 3 situações:

# Comprar apenas latas de 18 litros;
# Comprar apenas galões de 3,6 litros;
# Misturar latas e galões, de forma que o desperdício de tinta seja
# Menor. Acrescente 10% de folga e sempre arredonde os valores
# para cima, isto é, considere latas cheias.
import math

metros = float(input("Informe a quantidade em metros quadrado: "))
print(f'''OBS: As quantidades serão arrendondadas pra cima''')
folga = metros * 1.1
litros = folga / 6

capacidade_lata = 18
preco_lata = 80
total_lata = math.ceil(litros / capacidade_lata)
valor_total_lata = total_lata * preco_lata

capacidade_galao = 3.6
preco_galao = 25
total_galao = math.ceil(litros / capacidade_galao)
valor_total_galao = total_galao * preco_galao

latas = math.floor(litros / capacidade_lata)
litros_faltantes = litros % capacidade_lata
galoes = math.ceil(litros_faltantes / capacidade_galao)
valor_total_latas = latas * preco_lata
valor_total_galoes = galoes * preco_galao

print(f'''
Total metros quadrados: {folga:.2f} m²
Total litros a serem usados: {litros:.2f} L
-------------------------------------
-------------------------------------
1ª Situação apenas com latas:
--> {total_lata} lata(s) de {capacidade_lata} Litros
--> Valor total: R$ {(valor_total_lata):.2f}
-------------------------------------
2ª Situação apenas com galões:
--> {total_galao} galão(ões) de {capacidade_galao} Litros
--> Valor total: R$ {(valor_total_galao):.2f}
-------------------------------------
3ª Situação mesclando latas e galões:
{latas} lata(s) de {capacidade_lata} litros = R$ {(valor_total_latas):.2f}
{galoes} galão(ões) de {capacidade_galao} litros = R$ {(valor_total_galoes):.2f}
Valor total: R$ {(valor_total_galoes + valor_total_latas):,.2f}
''')