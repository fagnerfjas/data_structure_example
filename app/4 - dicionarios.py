dicionario = {
	'nome': 'Fagner',
	'idade': 34,
	'profissao': 'programador',
	'ativo': True
}

print(dicionario)
dicionario['endereco'] = 'Minha rua é '
print(dicionario)
print(dicionario['nome'])
dicionario['nome'] = 'Usuario do sistema'
print(dicionario)
del dicionario['profissao']
print(dicionario)

for key, value in dicionario.items(): 
	print(key + ' ----- ' + str(value))

print(dicionario.items())
print(dicionario.keys())
print(dicionario.values())