"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
"""

populacaoA = 80_000
populacaoB = 200_000

anos = 1
while populacaoA < populacaoB:
    taxa_anual_A = populacaoA * 0.03
    taxa_anual_B = populacaoB * 0.015
    populacaoA += taxa_anual_A
    populacaoB += taxa_anual_B
    print(f'{anos}º ano População A: {populacaoA:,.2f}. População B: {populacaoB:,.2f}')
    anos += 1
