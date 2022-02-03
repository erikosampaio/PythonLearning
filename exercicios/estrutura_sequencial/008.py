# Faça um Programa que pergunte quanto você ganha
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
hora_salario = float(input("Informe sua hora salarial: "))
numeros_horas_mes = float(input("Quantas horas você trabalha por mês: "))
salario_mes = hora_salario * numeros_horas_mes
print(f'No último mês trabalhado, seu salário foi R$ {salario_mes:.2f}')