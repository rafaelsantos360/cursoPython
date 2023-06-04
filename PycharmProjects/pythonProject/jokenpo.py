from time import sleep
from random import randint
item = ['Pedra', 'Papel', 'Tesoura']
computer = randint(0,2)
print('-=-'*25)
print('''Faça sua escolha!
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
print('-=-'*25)
jogador = int(input('Digite umas das opições acima: '))

print('\033[33mJO')
sleep(2)
print('\033[33mKEN')
sleep(2)
print('\033[33mPO!')
sleep(1)

print(f'\033[32mComputador escolheu {item[computer]}')
print(f'\033[35mJogador escolheu \033[35m{item[jogador]}')

if computer == 0:
    if jogador == 0:#prdra
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador GANHOU!')#papel
    else:
        print('Computador GANHOU')#tesoura
elif computer == 1:
    if jogador == 0:
        print('Computador GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    else:
        print('Jogador GANHOU!')
elif computer == 2:
    if jogador == 0:
        print('Jogador GANHOU!')
    elif jogador == 1:
        print('Computador GANHOU!')
    else:
        print('EMPATE!')
else:
    print('Aternativa invalida escolha outra ')

