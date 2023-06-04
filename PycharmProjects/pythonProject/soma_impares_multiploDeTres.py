valor = int(input('Digite valor: '))
s = 0
cont = 0
for n in range(1, valor+1, 2):
    if n % 3 == 0:
        cont += 1
        s += n
print(cont, s)