"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

populacaoA = int(input("Informe o valor da população A: "))
taxa_anual_A = float(input('Informe a taxa da população A: '))

populacaoB = int(input("Informe o valor da população B: "))
taxa_anual_B = float(input('Informe a taxa da população B: '))

anos = 1
while populacaoA < populacaoB:
    populacaoA += (populacaoA * taxa_anual_A)
    populacaoB += (populacaoB * taxa_anual_B)
    print(f'{anos}º ano População A: {populacaoA:,.2f}. População B: {populacaoB:,.2f}')
    anos += 1
