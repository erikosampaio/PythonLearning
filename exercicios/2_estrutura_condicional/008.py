# 2.8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Informe o valor do produto 1: "))
p2 = float(input("Informe o valor do produto 2: "))
p3 = float(input("Informe o valor do produto 3: "))

if p1 == p2 and p1 == p3:
    print(f'''
    Produtos com mesmo valor.
    Se atente para a qualidade!
    ''')
else:
    barato = p1
    if p2 < p1 and p2 < p3:
        print(f'Compre o produto no valor de R$ {p2:.2f}')
    elif p3 < p1 and p3 < p2:
        print(f'Compre o produto no valor de R$ {p3:.2f}')
    else:
        print(f'Compre o produto no valor de R$ {p1:.2f}')

# Ou em Pyhton:
print(f'Compre o produto no valor de R$ {min(p1, p2, p3):.2f}')
