# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Informe uma letra: ').lower()

if len(letra) != 1:
    print('Foi digitado mais de uma letra!')
elif letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Letra digitada é uma vogal!')
else:
    print('Letra digitada é uma consoante!')
