'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

my_tuple = ('CECI', 'JULIAN', 'SANTIAGO','DAMIAN')
for nombres in my_tuple:
  print(nombres)


product = {
  'name': 'Camisa',
  'price': 20000,
  'stock': 100
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'nombre': 'Nicolas',
    'edad': 34,
    'Descripcion': 'Ingeniero civil',
    'Hobby': "peliculas de creatividad"
  },
  {
    'nombre': 'Zuletta',
    'edad': 45,
    'Descripcion': 'POLICIA',
    'Hobby': "peliculas de criminalistica"
  },
  {
    'nombre': 'santi',
    'edad': 4,
  'Descripcion': 'Ingeniero de software',
  'Hobby': "peliculas de hacker"
  }
]

for person in people:
  print(person)

zoo = {
    'Leon': 8,
    'Jirafa': 5,
    'Hipo': 4,
}

for animal, cantidad in zoo.items():
    print(f'En el zoo tenemos: {animal} con una poblacion de {cantidad}')