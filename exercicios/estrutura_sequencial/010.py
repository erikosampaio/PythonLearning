# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.
c = float(input("Informe a temperatura em Celsius: "))

f = (c * 9 / 5) + 32

print(f'Graus em Celsius: {c}°C')
print(f'Graus em Fahrenheit: {f:.2f}°C')
