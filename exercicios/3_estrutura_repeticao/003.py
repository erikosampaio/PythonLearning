"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input('Nome com mais de 3 caracteres: ')
    print(len(nome))
    idade = int(input('Idade: '))
    salario = float(input('Salário: '))
    sexo = input('Sexo f/m: ').lower()
    estado_civil = input('Estado civil s/c/v/d: ')
    if len(nome) > 3:
        if 0 < idade < 150:
            if salario > 0:
                if sexo == 'f' or sexo == 'm':
                    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
                        print('Cadastro efetuado!')
                        break
    else:
        print('Todos os dados devem ser respeitados!')

