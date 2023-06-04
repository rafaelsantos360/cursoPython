cidade = input('DIgite cidade: ').strip().upper()
#dividir = cidade.split()

#print(f'Começa com a palavra santo\n{"SANTO" in dividir[0]}')
print(f'Começa com a palavra santo\n{cidade[:5] == "SANTO"}')
