from datetime import date
ano = int(input('Qual ano você quer analizar? Digite 0 para ano atual: '))
atual = date.today().year

if ano == 0:
    print(atual)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano é bissexto!')
else:
    print(f'O ano Não é bissexto!')