# Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.
lado = float(input("Informe o valor de um dos lados do quadrado: "))
area = lado ** 2
dobro_area = area * 2
print(f'Área do quadrado = {area:.2f}')
print(f'Dobro da área do quadrado = {dobro_area:,.2f}')
