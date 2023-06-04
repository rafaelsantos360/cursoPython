from datetime import date
atual = date.today().year
ano = int(input('Digite a sua ano: '))
idade = atual - ano

print(idade)

if idade < 18:
    print(f'Falta {idade - 18} anos para se alista!')
elif idade == 18:
    print('Já pode se alistar!')
else:
    print(f'Passou {idade - 18} anos da hora de se alistar!')