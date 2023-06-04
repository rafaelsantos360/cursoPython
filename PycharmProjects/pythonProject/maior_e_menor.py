a = int(input('Digite valor de "A"'))
b = int(input('Digite valor de "B"'))
c = int(input('Digite valor de "C"'))

if a > b and a > c:
    Mvalor = 'A'
    maior = a
elif b > a and b >c:
    Mvalor = 'B'
    maior = b
else:
    Mvalor = 'C'
    maior = c
menor = a

if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f'O {Mvalor} é o maior valor que é {maior}')
print(menor)