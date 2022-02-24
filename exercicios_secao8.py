# Número 1
"""def dobro(x):
    return x * 2


print(dobro(8))"""

# Número 2
"""def formatador_de_data(data):
    dia = data[0:2]
    mes = str(data[3:5])
    meses = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    mes = (meses[mes])
    ano = data[6:10]18/02
    return print(f' Você está no dia {dia} de {mes} de {ano}.')
    

formatador_de_data(input("Qual é a data em 'dd/mm/aaaa'?"))"""

# Número 3
"""def verificador_de_valor(valor):
    if valor >= 1:
        return 1
    elif valor <= -1:
        return -1
    return 0


print(verificador_de_valor(-5))"""

# Número 4
"""def quadrado_perfeito(x):
    x = x ** (1/2)
    if x > 0:
        x = str(x)
        zero = '.0'
        if x[1:3] == zero:
            return print('Esté número é um quadrado perfeito')
        elif x[2:4] == zero:
            return print('Este é um quadrado perfeito')
    return print('Esté numero NÃO é um quadrado perfeito')
        

quadrado_perfeito(2)"""

# Número 5
"""def calculo_volume_esfera(r):
    pi = 3.1415
    v = 4/3 * pi * (r ** 3)
    return print(f'Uma esefa de raio {r} tem {v} de volume')


calculo_volume_esfera(5)"""

# Número 6
"""def conversor_para_segundos(h,m,s):
    m = m + (h * 60)
    s = s + (m * 60)
    return (print(f'{s} segundos'))


conversor_para_segundos(int(input('Qual a hora?')), int(input('Qual os minutos?')), int(input('Qual os segundos?')))"""

# Número 7
"""def conv_celsios_fahreheind(c):
    f = c * (9/5) + 32
    return print(f)


conv_celsios_fahreheind(60)"""

# Número 8 e 9 iguais a 7

# Número 10
"""def maior(a,b):
    if a > b:
        return print('O primeiro número é maior que o segundo')
    return print('O segundo número é maior que o primeiro')

maior(6,5)"""

# Número 11
"""def media(x,y,z,tipo = 'a'):
    if tipo == 'a':
        media = (x + y + z) / 3
        return (print(media))
    elif tipo == 'p':
        x = x * 5
        y = y * 3
        z = z * 2
        media = (x + y + z) / 10
        return (print(media))
    return print('O tipo de avaliação está incorreto')


media(10,8,0)
media(10,2,2,'p')
media(2,2,2,'j')"""

"""PAUSA PARA COMPREHENSION"""
import random
for i in range (9):
    print(random.randrange(0,9,1))

# é o mesmo que
print('pausa')

[print(random.randrange(0,9,1)) for i in range(9)]


