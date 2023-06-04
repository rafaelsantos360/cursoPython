import random
n1 = input('Digite 1° nome: ')
n2 = input('Digite 2° nome: ')
n3 = input('Digite 3° nome: ')
n4 = input('Digite 4° nome: ')
lista = [n1, n2, n3, n4]
escolha = random.choice(lista)

print('O aluno selecionado é {}'.format(escolha))