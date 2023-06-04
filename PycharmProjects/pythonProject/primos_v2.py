v = int(input('Digite numero: '))
primos = 0
for n in range(1, v+1):
    if v % n == 0:
        primos += 1
        print(v % n)
if primos <= 2:
    print('Primo')
else:
    print('Não é primo!')