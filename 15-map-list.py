items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]
print("====>")
prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)
print("====>")
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item
print("====>")
new_items = list(map(add_taxes, items))
print(new_items)
print(items)