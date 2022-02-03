def contar_caracteres(s):
    """Função que conta os caracteres iguais de uma string."

    Ex:

    >>> contar_caracteres('renzo')
    e: 1
    n: 1
    o: 1
    r: 1
    z: 1
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada
    """
    caracteres_ordenados = sorted(s)

    car_anterior = caracteres_ordenados[0]
    con = 1

    for caracter in caracteres_ordenados[1:]:
        if car_anterior == caracter:
            con += 1
        else:
            print(f'{car_anterior}: {con}')
            con = 1
        car_anterior = caracter
    print(f'{car_anterior}: {con}')


if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))
