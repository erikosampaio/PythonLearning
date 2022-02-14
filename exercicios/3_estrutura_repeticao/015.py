"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n = int(input("Informe um termo para a série de Fibonacci: "))
t1 = 1
t2 = 1
print(f"{t1} --> {t2}", end=' --> ')
con = 3
while con <= n:
    t3 = t1 + t2
    print(f"{t3}", end=' --> ')
    t1 = t2
    t2 = t3
    con += 1
print('Fim!')
