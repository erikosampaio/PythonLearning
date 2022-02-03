def contar_caracteres(s):
    """Função que conta os caracteres iguais de uma string."

    Ex:

    >>> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    """

    resultado = {}

    for caracter in s:
        print(f'Dict antes do for: {resultado}')
        print(f'Caracter: {caracter}')
        resultado[caracter] = resultado.get(caracter, 0) + 1
        print(f'Chave recebida: {resultado[caracter]}')
        print(f'Dict após o for: {resultado}')
        print()
        print()
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))
    # print(contar_caracteres('banana'))
