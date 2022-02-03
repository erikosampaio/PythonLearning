# Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) Salário bruto.
# b) Quanto pagou ao IR.
# c) Quanto pagou ao INSS.
 #d) Quanto pagou ao sindicato.
# e) O salário líquido.

ganho_hora = float(input("Informe seu ganho por hora: "))
horas_trabalhadas_mes = int(input("Informe quantas horas você trabalhou no mês: "))

total_salario_bruto = ganho_hora * horas_trabalhadas_mes
ir = total_salario_bruto * 0.11
inss = total_salario_bruto * 0.08
sindicato = total_salario_bruto * 0.05
total_salario_liquido = total_salario_bruto - ir - inss - sindicato

print(f'''
Salário bruto --> R$ {total_salario_bruto:,.2f}
Quanto pagou ao IR --> R$ {ir:.2f}
Quanto pagou ao INSS --> R$ {inss:.2f}
Quanto pagou ao sindicato --> R$ {sindicato:.2f}
O salário líquido --> R$ {total_salario_liquido:,.2f}
''')
