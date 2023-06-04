valor = int(input('Digite valor: '))
soma = 0
cont = 0
for c in range(1, valor+1):
    num = int(input('Digite número: '))
    if num % 2 == 0:
        cont += 1
        soma += c
print('Soma dos pares é {} e os numeros domados foram {}'.format(soma, cont))