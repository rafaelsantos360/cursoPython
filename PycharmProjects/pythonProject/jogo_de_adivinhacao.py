from random import randint
from time import sleep
aleatorio = randint(1, 5) #computador vai penssar em um número
print('-=-' * 20)
print('Vou pençar de 1 a 5:')
print('-=-' * 20)
valor = int(input('Digite valor: '))#jogador vai adivinhar o valor gerado pelo cpmputador
print('Processando...')
sleep(3)

if valor == aleatorio:
    print('Ganhou!')
else:
    print('Perdeu!')