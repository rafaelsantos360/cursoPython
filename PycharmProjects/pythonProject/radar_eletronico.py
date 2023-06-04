velocidade = float(input('Digite velocidade atual Km/h: '))

if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado! Você exedeu o limite de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa a ser pago é R${multa}')