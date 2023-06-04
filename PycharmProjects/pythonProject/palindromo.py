frase = input('Digite frase: ').strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = juntar[::-1]
'''for c in range(len(juntar) -1, -1, -1):
    inverso += juntar[c]'''
if inverso == juntar:
        print('Verdadeiro')
else:
        print('Falso')


