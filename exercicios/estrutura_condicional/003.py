# 2.3 Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite uma letra: ").upper()

if letra == 'F':
    print('Feminino')
elif letra == 'M':
    print('Masculino')
else:
    print('Sexo inválido')
