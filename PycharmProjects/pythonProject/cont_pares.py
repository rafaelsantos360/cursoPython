valor = int(input('Digite valor: '))
#for c in range(1, valor+1):
#    if c % 2 == 0:
#        par = c
#        print('.', end=' ')
#        print(par, end=' ')
for n in range(2, valor+1, 2):
    print('.', end=' ')
    print(n, end=' ')