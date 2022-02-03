def valida(ip: str):
    numeros = ip.split('.')

    if len(numeros) != 4:
        return False

    for n in numeros:
        if not (0 <= int(n) <= 255):
            return False
    return True


ips_validos = []
ips_invalidos = []
with open('/content/drive/MyDrive/DevPro/Projetos/Exercícios/ips.txt', 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        # print(ip, valida(ip))
        if valida(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open('/content/drive/MyDrive/DevPro/Projetos/Exercícios/ips_saida.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')

    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços inválidos:]\n')

    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')
