from math import floor, trunc

valor = float(input('Digite 1° valor a redondadr: '))
valor2 = float(input('Digite 2° valor a redondadr: '))
v3 = float(input('Digite 3° valor: '))
print('O valor {} arredondado vai ser {}'.format(valor, floor(valor)))
print('O 2° valor {} arredondado é {}'.format(valor2, trunc(valor2)))
print('O 3° valor {} arredondado e {}'.format(v3, int(v3)))