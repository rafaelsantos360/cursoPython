n1 = int(input("Digite um valor: "))
n2 = int(input('Digite outro valor: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1%n2

print("O valor da soma {}\n da multiplicação {}\n divição {:.3f} da ".format(s, m, d), end='')
print("divição inteira {} e resto da diviçao {}".format(di, e) )