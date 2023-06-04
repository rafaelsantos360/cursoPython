from datetime import date
print('\033[33m-=-' * 20)
print('                  \033[32mClassificando atletas')
print('\033[33m-=-' * 20)
atual = date.today().year
ano = int(input('\033[35mDigite ano: '))
idade = atual - ano
print(idade)

if idade >= 9 and idade < 14:
    print('\033[33mMIRIM')
elif idade < 19:
    print('\033[32mINFANTIL')
elif idade < 20:
    print('\033[35mJUNIOR')
elif idade == 20:
    print('\033[36mSÊNIOR')
else:
    print('\033[37mMASTER')