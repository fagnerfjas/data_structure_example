
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
cars.reverse()
print(cars)
cars.sort(reverse=True)
print('tamanho da lista: ' + str(len(cars)))

print('-------------------------------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

fruits = ['banana', 'apple', 'passion fruit']

print(fruits[1].upper())
print(fruits[-1])
fruits[1] = "orange"
fruits.append("watermelon")
print(fruits)
print('--------- Adicionando mais coisas na lista')
fruits.insert(0, 'grape')
fruits.insert(2, 'pinaple')
print(fruits)

print('--------- removendo o quarto ítem')
del fruits[4]
print(fruits)

print('---------------------------------')
# Operações matemáticas
age = 32
print("Feliz aniversario de " + str(age) + " anos")
print(4+4)
print(10-2)
print(64/8)
print(2*4)

'''
	Comentário para várias linhas me python
'''

# Contas atividade 2
print('---------------------------------')
print(2*5+3)
print(0.2+0.1)

# Strings atividade 3 
print('---------------------------------')
nome = "fagner "
sobrenome = "jefferson"
fullname = nome + sobrenome

nome = nome.rstrip()
fullname = nome + sobrenome

print( '\t' + fullname.upper() + '\n\tEsse é seu nome' )

message = "Melhor mensagem Manu's bar"
print(message)