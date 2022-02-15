"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

c1 = 0
c2 = 0
c3 = 0

total_eleitores = int(input("Informe o total de eleitores: "))

for i in range(total_eleitores):
    escolha = int(input("Digite: \n\t1 - Candidato 1\n\t2 - Candidato 2\n\t3 - Candidato 3\n\tOpção: "))
    if escolha == 1:
        c1 += 1
    elif escolha == 2:
        c2 += 1
    elif escolha == 3:
        c3 += 1

print(f'Votos do candidato 1: {c1}')
print(f'Votos do candidato 1: {c2}')
print(f'Votos do candidato 1: {c3}')
