l1 = int(input('Digite 1° linha: '))
l2 = int(input('Digite 2° linha: '))
l3 = int(input('Digite 3° linha: '))

if l1 == l2 and l2 == l3:
    print('Equilátero!')
elif l1 + l2 < l3 or l2 + l3 < l1 or l3 + l1 < l2:
    print('Isósceles!')
else:
    print('Escaleno!')