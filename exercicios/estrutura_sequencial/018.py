# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).
import math

tamanho = float(input("Informe o tamanho do arquivo em MB: "))
velocidade = float(input("Informe a velocidade do link em Mbps: "))

minutos = math.floor(tamanho / (velocidade * 60))
segundo = tamanho % (velocidade * 60)
while segundo >= 60:
    minutos += 1
    segundo -= 60

if minutos > 0:
    if segundo > 0:
        print(f'o donwload levará {minutos} minuto(s) e {segundo} segundo(s) para ser baixado completamente!')
    else:
        print(print(f'o donwload levará {minutos} minuto(s) para ser baixado completamente!'))
else:
    print('Informações inválidas!')

