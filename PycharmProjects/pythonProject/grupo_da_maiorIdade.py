from datetime import date
maior = 0
menor = 0
for c in range(0, 4):
    ano = int(input('Digite ano: '))
    data = date.today().year
    idade = data - ano
    if idade < 18:
        maior += 1
    else:
        menor += 1

print(f'Ao todo temos {menor} maiores de idade')
print(f'E temos {maior} menores de idade')
