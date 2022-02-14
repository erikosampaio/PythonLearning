class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self,):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    eriko = Pessoa(nome='Eriko')
    luciano = Pessoa(eriko, nome='Luciano')
    # print(id(luciano))
    # print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)
    print(eriko.__dict__)
    print(luciano.__dict__)
    del luciano.filhos
    print(luciano.__dict__)
