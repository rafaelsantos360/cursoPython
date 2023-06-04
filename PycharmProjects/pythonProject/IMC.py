peso = float(input('Digite peso: '))
altura = float(input('Digite altura: '))
imc = peso / altura ** 2

print(imc)

if imc < 18:
    print('\033[1:35mAbaixo do peso!')
elif imc <= 25:
    print('\033[1:34mPeso ideal!')
elif imc <= 40:
    print('\033[1:33mAcima do peso!')
else:
    print('\033[1:31mObesidade!')