"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas
e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

while True:
    turmas = int(input("Quantas turmas você define: "))
    if turmas <= 0:
        print('Número de turmas deve ser maior que 0!')
    else:
        break

alunos_por_turma = 0
total_alunos = 0
i = 0
while i < turmas:
    alunos_por_turma = int(input(f"Quantas alunos terá a turma {i+1}: "))
    if alunos_por_turma < 0:
        pass
    else:
        total_alunos += alunos_por_turma
        i += 1

media_alunos_por_turma = total_alunos / turmas

print(f'Existem {turmas} Turmas e {total_alunos} alunos')
print(f'A média de alunos por turma é {media_alunos_por_turma:.2f}')
