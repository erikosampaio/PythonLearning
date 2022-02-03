# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de
# espaço em disco no seu servidor de arquivos. Para tentar resolver este
# problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
# usuários, e identificar os usuários com maior espaço ocupado.
# Através de um programa, baixado da Internet, ele conseguiu gerar
# o seguinte arquivo, chamado "usuarios.txt":
#
# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125
#
#
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
# você deve criar um programa que gere um relatório,
# chamado "relatório.txt", no seguinte formato:
#
#
# ACME Inc. Uso do espaço em disco pelos usuários
# --------------------------------------------------------------
# Nr. Usuário     Espaço utilizado    % do uso
#
# 1 alexandre         434,99 MB        16,85%
# 2 anderson         1187,99 MB        46,02%
# 3 antonio           117,73 MB        4,56%
# 4 carlos             87,03 MB        3,37%
# 5 cesar               0,94 MB        0,04%
# 6 rosemary           52,88 MB        29,16%
#
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
#
#
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de
# forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá
# ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de
# uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

def transformar_em_megabytes(tamanho_em_bytes: str) -> float:
    return int(tamanho_em_bytes) / (2 ** 10) ** 2


def percentual(tamanho_em_disco, tamanho_total_discos):
    return f'{tamanho_em_disco / tamanho_total_discos:6.2%}'


lista_de_dados = []
with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((usuario, tamanho_em_disco))

cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
'''
with open('relatorio.txt', 'w') as arquivo:
    arquivo.writelines(cabecalho)
    tamanho_total_discos = sum([tamanho for _, tamanho in lista_de_dados])
    soma = tamanho_total_discos / len(lista_de_dados)
    for indice, dados in enumerate(lista_de_dados, start=1):
        usuario, tamanho_em_disco = dados
        arquivo.writelines(
            f'{indice:<4} {usuario.title()} {tamanho_em_disco:>9.2f} MB         '
            f'{percentual(tamanho_em_disco, tamanho_total_discos)}\n'
        )

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_discos:.2f} MB')
    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço médio ocupado: {soma:.2f} MB')
