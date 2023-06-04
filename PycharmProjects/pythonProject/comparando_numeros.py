n1 = int(input('Digite 1° valor: '))
n2 = int(input('Digite 2° valor: '))

if n1 > n2:
    print(f'O 1° valor que é {n1} é maior que 2° valor que é {n2}')
elif n2 > n1:
    print(f'O 2° valor que é {n2} é maior que 1° valor que é {n1}')
else:
    print('\033[1:31mValor são iquais!')
