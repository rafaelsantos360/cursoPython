nome = input('Digite se nome: ').strip()
dividir = nome.split()

print(f'Seu nome em maiusculo é {nome.upper()}')
print(f'Seu nome em minusculo é {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome é {dividir[0]} e tem {len(dividir[0])} letras')