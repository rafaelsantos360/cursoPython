import random
computer = random.choice(['pedra', 'papel', 'tesoura'])
print(computer)
jogador = input('Digite sua opição: ')

if computer == 'papel' and jogador == 'pedra' or computer == 'pedra' and jogador == 'tesoura' or computer == 'tesoura' and jogador == 'papel':
    print('Computador Ganhou!')
elif jogador == 'papel' and computer == 'pedra' or jogador == 'pedra' and computer == 'tesoura' or jogador == 'tesoura' and computer == 'papel':
    print('Jogador Ganhou!')
else:
    print('EMPATE!')