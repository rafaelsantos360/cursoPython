tab = int(input('Digite tabuada: '))
v = int(input('Valor a multiplicar: '))
for c in range(1, v+1):
    s = tab * c
    print(f'{tab} X {c} = {s}')
