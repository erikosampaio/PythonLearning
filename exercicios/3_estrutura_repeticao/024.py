"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

num = int(input("Quantas notas informadas: "))
notas = []

for i in range(num):
    notas.append(float(input(f"Nota {i+1}/{num}: ")))

print(f'Notas = {notas}')
print(f'Média = {sum(notas) / len(notas):.2f}')
