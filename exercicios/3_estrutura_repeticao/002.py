# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
# usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    nome = input('Informe seu nome: ')
    senha = input('Informe sua senha: ')
    if nome != senha:
        print('Login efetuado!')
        break
    else:
        print('Senha não pode ser igual ao usuário!')
