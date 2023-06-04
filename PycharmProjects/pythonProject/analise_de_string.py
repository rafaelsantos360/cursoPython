nome = input('Digite seu nome: ').upper()
divi = nome.split()
print(f'Seu primeiro nome é {divi[0]}')
print(f'Seu ultimo nome é {divi[len(divi) - 1]}')