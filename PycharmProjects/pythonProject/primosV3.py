valor = int(input('Digite valor: '))
primo = 0


for n in range(1, valor+1):
    if valor % n == 0:
        print(f'\033[34m{n}\033[34m ', end= ' ')
        primo += 1
    else:
        print(f'\033[31m{n}\033[31m', end= ' ')
print(f'\033[0mA soma do das devisões de numero {valor} é {primo} ')
if primo == 2:
    print('Esse numero é primo!')
else:
    print('Esse numero não é primo!')