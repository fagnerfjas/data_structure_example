'''
	Condicionais em python 
'''

cars = ['fusca', 'pegeout', 'Camaro', 'opala']

if ('Camaro' in cars) or False: 
	print('existe')

car = 'subaru'
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi') 

print('--------------------------- if else')
age = 3.5
if age >= 7 and age <= 10:
	print('Passou direto')
elif age < 7 and age > 4: 
	print('recuperacao')
else:
	print('reprovado')