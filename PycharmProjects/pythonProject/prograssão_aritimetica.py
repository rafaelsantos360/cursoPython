prim = int(input('Digite primeiro termo: '))
vezes = int(input('Digite quantas vezes: '))
razao = int(input('Digite razao: '))
termo = prim + (vezes - 1) * razao

for c in range(prim, termo, razao):
    print(f'{c}', end='->')
    #print('->', end=' ')
print('Acabou!')