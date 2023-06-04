nome = input('Digite nome: ').strip().upper()

print(f'Quantida de A no nome é {nome.count("A")}')
print(f'A primeira letra "A" está na possição {nome.find("A") + 1}')
divi = nome.split()
print(f'Ultima letra "A" está na possição {nome.rfind("A")}')