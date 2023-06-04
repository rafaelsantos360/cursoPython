valor = int(input('Digite valor: '))
c = 1
res = 0


while c <= valor:
    if valor % c == 0:
        res += 1
    c += 1
    print(valor % c)
if res <= 2:
    print('Primo!')
else:
    print('Não é primo!')

