print('1: AVISTA Dinheiro/cheque')
print('2: AVISTA No cartão 5% de Desconto')
print('3: 3x ou mais 20% de juros')
op = int(input('Digite uma das opções: '))
valor = float(input('Digite valor a pagar: '))

if op == 1:
    print(f'O valor pago a vista Dinheiro/cheque será {valor - valor * 10 / 100}')
elif op == 2:
    print(f'O valor a vista no cartão é {valor - valor * 5 / 100}')
else:
    print(f'3x ou mais 20% de juros será {(valor + valor * 20 / 100) / 3}')