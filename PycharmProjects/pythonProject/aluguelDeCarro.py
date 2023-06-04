logo = 'Aluguel de carros'
print('{}'.format(logo))
dias = float(input("Digite quantos dias: "))
km = float(input("Digite quantos kilometros: "))
valor = 90*dias+km*0.25
print("O valor alugado será R${:.2f}".format(valor))