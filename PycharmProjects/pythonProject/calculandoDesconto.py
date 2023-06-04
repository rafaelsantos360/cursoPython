valor = float(input("Digite valor do produto: "))
porcent = float(input("Digite valor do descont"))
desc = float(valor-(valor*porcent)/100)

print("O valor á descontar é {}".format(desc))