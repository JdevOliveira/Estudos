import random

# Número 1
"""A = [1, 0, 5, -2, -5, 7]
print(A)
soma = sum(A[0:3])
print(soma)
A[3] = 100
print (A)"""

# Número 2
"""A = input('Qual o valor?')
B = input('Qual o valor?')
C = input('Qual o valor?')
D = input('Qual o valor?')
E = input('Qual o valor?')
F = input('Qual o valor?')
valores = A, B, C, D, E, F
print(valores)"""

# Número 3
"""Vetor1 = (2, 4, 5, 2, 5, 6, 7, 3, 1, 5)
Vetor2 = []
for n in Vetor1:
    Vetor2.append(n ** 2)
    if len(Vetor2) == 10:
        print(Vetor2)"""

# Número 4
"""Vetor = [3, 6, 2, 7, 2, 9, 1, 3]
S = [0, 1, 2, 3, 4, 5, 6, 7]
Xis = random.choice(S)
Yip = random.choice(S)
print(f'Primeiro valor aleatorio {Xis}')
print(f'Segundo valor aleatório {Yip}')
Valor1 = Vetor[Xis]
Valor2 = Vetor[Yip]
print(Valor1)
print(Valor2)
Soma = Valor1 + Valor2
print(Soma)"""

# Número 5
"""Vetor =list(range(0, 10))
k = []
for i in Vetor:
    j = i % 2
    if j == 0:
        k.append(i)
        print(len(k))"""

# Número 6
"""Vetor = list(range(0, 10))
print(min(Vetor))
print(max(Vetor))"""

# Número 7
"""vetor = [0, 22, 4, 11, 56, 12, 5, 66, 32, 8]
x = max(vetor)
y = vetor.index(max(vetor))
print(x)
print(y)"""

# Número 8
"""x = list(range(0, 8))
x.reverse()
print(x)"""

# Número 9
"""x = list(range(2, 13, 2))
x.reverse()
print(x)"""

# Número 10
"""x = [random.randrange(0, 10, 1) for i in range(15)]
print(x)
y = sum(x) / 15
print (y)"""

# Número 11
"""x = [random.randrange(-10, 10, 1) for i in range(10)]
y = []
z = []
print(x)
for i in x:
    if i < 0:
        y.append(i)
    else:
        z.append(i)
        
print(len(y))
print(sum(z))"""

# Número 12
"""x = [random.randrange(0, 30) for i in range(5)]
print(x)
print(min(x))
print(max(x))
print(sum(x)/5)"""

# Número 13
"""x = [random.randrange(0,10) for i in range(5)]
print(x)
print(x.index(max(x)))
print(x.index(min(x)))"""

# Número 14
"""x = [random.randrange(0, 11) for i in range (10)]
print (x)
# y = set(x)
# y = list(y) - NÃO DEU CERTO!
# print(y)
from collections import Counter
y = Counter(x)
print(y)
for key, value in y.items():
    if value > 1:
        print(key)"""

# Número 15
"""x = [random.randrange(0, 15) for i in range (20)]
print (x)
y = set(x)
k = list(y)
print (k)"""

# Número 16
"""x = [random.randrange(0, 6) for i in range (6)]
print(x)
y = sorted(x)
print(y)"""

# Número 17
"""x = [random.randrange(-5, 5) for i in range (10)]
print(x)
y = []
for i in x:
    if i > 0:
        y.append(i)
    else:
        y.append(0)
print(y)"""

# Número 18
"""x = [random.randrange(0,30) for i in range(10)]
print(x)
y = random.choice(x)
print(y)
for y in range (y, y*10, y):
    print(y)"""

# Número 19
"""i = int(input('Qual o valor de i?'))
valor = (i+5*5)%(i+1)
vetor = []
for valor in range (valor, valor+50):
    vetor.append(valor)
print(vetor)
y = vetor.index(i)
print(i)"""

# Número 20
"""x = [random.randrange(0,50) for i in range (10)]
print(x)
y = []
for i in x:
    j = i % 2
    if j != 0:
        y.append(i)
print(y)"""
