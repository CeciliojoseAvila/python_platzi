file = open('./texto.txt')
print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())


"""
for line in file:
  print(line)

file.close()
 """

""" 
 la sgte linea con with hace que python cierre el archivo automaticamente
 """ 

with open('./texto.txt') as file:
  for line in file:
    print(line)
