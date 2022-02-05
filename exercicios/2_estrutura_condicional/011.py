# As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os
# reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste
# segundo o seguinte critério, baseado no salário atual:

# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5%.

# Após o aumento ser
# realizado, informe na tela:

# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - novo valor do aumento;
# - o novo salário, após o aumento.

inicial = float(input("Informe seu salário: "))

if inicial <= 0:
    print('Não há reajuste salarial!')
else:
    if inicial <= 280:
        taxa = inicial * 0.2
        percentual = '20%'
    elif 280 < inicial <= 700:
        taxa = inicial * 0.15
        percentual = '15%'
    elif 700 < inicial <= 1500:
        taxa = inicial * 0.1
        percentual = '10%'
    else:
        taxa = inicial * 0.05
        percentual = '5%'

    final = inicial + taxa

    print(f'''
    - O salário antes do reajuste: R$ {inicial:,.2f}
    - O percentual de aumento aplicado: {percentual}
    - O valor do aumento: R$ {taxa:.2f}
    - O novo salário, após o aumento: R$ {final:,.2f}
    ''')
