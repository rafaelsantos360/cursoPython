num = int(input('Digite numero: '))
print('''Escolha uma base para conversão
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')
op = int(input('Selecione uma opiçaõ: '))

if op == 1:
    print(f'O valor binario de {num} é {bin(num) [2:]}')
elif op == 2:
    print(f'O valor octal de {num} é {oct(num) [2:]}')
elif op == 3:
    print(f'O valor hexadecimal de {num} é {hex(num) [2:]}')
else:
    print(f'Valor Invalido!')