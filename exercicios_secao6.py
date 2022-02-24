# Número 1
"""for numero in range(3,16,3):
    print(numero)"""

# Número 2
"""for numero in range (0,101):
    print (numero)
numero2 = 0
while numero2 < 100:
    numero2 = numero2 + 1
    print(numero2)"""

# Número 3
"""numero = 11
while numero > 0:
    numero = numero - 1
    print (numero)
    if numero == 0:
        print('Fim')"""

# Número 4
"""for num in range(0,100001,1000):
    print(num)"""

# Número 5
"""contagem = 0
soma = 0
while contagem < 10:
    contagem = contagem + 1
    numero = int(input(f'Qual o numero {contagem}?'))
    soma = soma + numero
    if contagem == 10:
        print(soma)"""

# Número 6
"""contagem = 1
valor = 0
while contagem < 11:
    numero = int(input(f'Qual o número {contagem}?'))
    valor = numero + valor
    contagem = contagem + 1
    if contagem == 11:
        media = valor / 10
        print(f'A média é {media}')"""

# Número 7
"""contagem = 0
valor = 0
positivos = 0
divisor = 0
while contagem < 10:
    contagem = contagem + 1
    numero = int(input(f'Qual o número {contagem}?'))
    if numero >= 0:
        valor = numero + valor
        positivos = positivos + 1
        if contagem == 10:
            print(positivos)
            media = valor / positivos
            print(f'A média é {media}')
    divisor = divisor + positivos"""

# Número 8
"""valor_maior = valor_menor = int(input('Digite o 1º valor: '))
for cont in range(2, 11):
    numero = int(input(f'Digite o {cont}º valor: '))
    if numero >= valor_maior:
        valor_maior = numero
    else:
        valor_menor = numero
print(f'Maior: {valor_maior}\nMenor: {valor_menor}')""" 

# Número 9
"""numero = int(input('Qual é o número?'))
par = numero % 2
vezes = numero * 3
if par != 0:
    for numero in range(numero, vezes , 2):
        print (numero)
else:
    for numero in range(numero+1, vezes+1, 2):
        print (numero)"""

# Número 10
"""i = sum (range (0 , 51 , 2))
print (i)"""

# Número 11
"""n = int(input('Qual é o valor?'))
for num in range(0,n+1,1):
    print (num)"""

# Número 12
"""n = int(input('Qual é o valor?'))
for num in range(n,-1,-1):
    print (num)"""

# questões iguais

# Número 21
n1 = int(input('Qual o primeiro número?'))
n2 = int(input('Qual o segundo número?'))
par1 = n1 % 2
par2 = n2 % 2
vez = 1
print (par1)
print (par2)
if par1 == 0 and par2 == 0:
    inicio = min(n1,n2)
    fim = max(n1,n2)
    soma = sum(range(inicio,fim+1,2))
    print (f'O valor da soma é {soma}')
    for i in range(inicio+1, fim+1, 2):
        vez = i * vez
        if i == fim-1:
            vezes = n1 * n2 * vez
            print(f'O valor da multiplicação é {vezes}')
elif par1 != 0 and par2 !=0:
    inicio = min(n1,n2)
    fim = max(n1,n2)
    soma = sum(range(inicio+1,fim+1,2))
    somao = soma + n1 + n2
    print (f'O valor da soma é {somao}')
    for i in range(inicio, fim+1, 2):
        vez = i * vez
        if i == fim:
            #vezes = n1 * n2 * vez
            print(f'O valor da multiplicação é {vez}')
else:
    inicio = min(n1,n2)
    fim = max(n1,n2)
    fimreal = fim % 2
    if fimreal == 0:
        soma = sum(range(inicio,fim+1,2))
    print (f'O valor da soma é {soma}')
    for i in range(inicio+1, fim+1, 2):
        vez = i * vez
        if i == fim-1:
            vezes = n1 * n2 * vez
            print(f'O valor da multiplicação é {vezes}')
    
# Número 22
