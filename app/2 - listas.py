print('cubos Comprehensio --------------------------------------')
print([i**3 for i in range(1, 11)])

print('cubos --------------------------------------')
for i in range(1, 11):
	print(i**3)

print('--------------------------------------')
for i in range(3, 31, 3):
	print(i)

print('--------------------------------------')
for i in range(1, 21, 2):
	print(i)

digits = list(range(10));

print(digits)
print('minimo ' + str(min(digits)))
print('maximo ' + str(max(digits)))
print('soma ' + str(sum(digits)))

squares = [value**2 for value in range(1,21, 2)]

print(squares)

list_milion = list(range(1,21))

print(min(list_milion))
print(max(list_milion))
print(sum(list_milion))

print('----------------------------- Partes de uma lista')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('lista inteira: ' + str(players))
print(players[2:4])
print(players[:4])
print(players[-3:])

print('----------------------------- Copiando lista')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
jogadores = players[-2:]
print(jogadores)

lista2 = jogadores
print(lista2)

print('---------------------------- TUPAS')
quadrado = (30, 30);

print(quadrado)