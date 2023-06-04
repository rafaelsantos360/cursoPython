a = int(input('Digite valor da 1° linha: '))
b = int(input('Digite valor da 2° linha: '))
c = int(input('Digite valor da 3° linha: '))

if a != b and b != c:
    print('Triangulo!')
elif a + b <= c or b + c <= a or c + a <= c:
    print('Asocilis!')