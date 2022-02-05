class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self,):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    eriko = Pessoa(nome='Eriko')
    luciano = Pessoa(eriko, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())  # Forma mais fácil do primeiro print.
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(eriko.__dict__)
    print(luciano.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(eriko.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(eriko.olhos))
