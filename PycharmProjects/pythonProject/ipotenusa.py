from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adijasente: '))
'''ip = (co ** 2 + ca ** 2) ** (1 / 2)
print('o o valor da ipotenuza é {}'.format(ip))'''
hi = hypot(co, ca)
print('A hiphotenuza é {}'.format(hi))
