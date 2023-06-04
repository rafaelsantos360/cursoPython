from datetime import date
soma = 0
maior = 0
velho = ''
for c in range(1, 5):
    atual = date.today().year
    print(f'{c}° sessão')
    nome = input('Digite seu nome: ').strip().upper()
    nasc = int(input('Digite data de nascimento: '))
    sexo = input('Digite genero [M/F]: ').upper()
    idade = atual - nasc
    soma += idade
    if idade > maior and sexo == 'M':
        velho = nome
        maior = idade
        genero = 'Homem'
    else:
        velho = nome
        maior = idade
        genero = 'Mulher'

    print(soma)

media = soma / c
print(f'''A media do glupo é {media} anos
O {genero} mais velho/a é {velho} de {maior} anos''')
