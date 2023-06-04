nome = input("Digite nome do funcionario: ")
valorPorcentagem = float(input('Digite valor do reajuste: %'))
salarioAtual = float(input('Digite salário atual: R$'))
ajuste = float(salarioAtual+(salarioAtual*valorPorcentagem)/100)

print("O total do reajuste do funcionario {} é R${}".format(nome, ajuste))