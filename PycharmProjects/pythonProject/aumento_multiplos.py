sal = float(input('Digite salário: '))

if sal >= 1240:
    soma = sal * 10 / 100 + sal
else:
    soma = sal * 15 / 100 + sal
print(f'Total do salario com aumento é {soma}')