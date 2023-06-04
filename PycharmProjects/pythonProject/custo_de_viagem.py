viagem = int(input('Digite Kilometrôs percorridos: '))
tot = viagem * 0.50
if viagem > 200:
    tot = viagem * 0.45
    print(f'Acima de 200Km/h o valor é {tot}')
print(f'Valor {viagem} é {tot}')