# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
#
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valor = int(input("Valor da sua hora de trabalho: "))
horas = int(input("Informe quantas horas foram trabalhadas: "))

bruto = valor * horas

if bruto <= 0:
    print('Não há cálculo para ser feito!')
else:
    if bruto <= 900:
        ir = 0
        inss = bruto * 0.1
        p = ''
        fgts = bruto * 0.11
    elif 900 < bruto <= 1500:
        ir = bruto * 0.05
        p = '5%'
        inss = bruto * 0.1
        fgts = bruto * 0.11
    elif 1500 < bruto <= 2500:
        ir = bruto * 0.1
        p = '10%'
        inss = bruto * 0.1
        fgts = bruto * 0.11
    else:
        ir = bruto * 0.2
        p = '20%'
        inss = bruto * 0.1
        fgts = bruto * 0.11

    descontos = ir + inss
    liquido = bruto - descontos

    print(f'''
    Salário Bruto:({valor} * {horas})         : R$ {bruto:,.2f}
    (-) IR ({p})                     : R$ {ir:.2f}
    (-) INSS (10%)                   : R$ {inss:.2f}
    FGTS (11%)                       : R$ {fgts:.2f}
    Total de descontos               : R$ {descontos:.2f}
    Salário Liquido                  : R$ {liquido:,.2f}
    ''')
