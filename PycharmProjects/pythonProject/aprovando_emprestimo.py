sal = float(input('Digite valor do salario: R$'))
emp = float(input('Digite valor do emprestimo: R$'))
par = int(input('Digite quantas vezes será as parcelas: '))
totP = emp / par

print('Total das parcelas é R${:.2f} {:.2f}%'.format(totP, totP / sal * 100))

if totP / sal * 100 <= 30:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo reprovado!')
