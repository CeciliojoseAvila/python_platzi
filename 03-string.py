my_name = "Cecilio"
my_last_name = "Avila Ramos"
my_age = 36

quote1 = f"Hola mi nombre es {my_name} y mi apellido es {my_last_name}, tengo {my_age} años"
print(quote1)

quote2 = "Hola mi nombre es " + my_name + " y mi apellido es " + my_last_name + ", tengo " + str(my_age) + " años"
print(quote2)

quote3 = "Hola mi nombre es {} y mi apellido es {}, tengo {} años" .format(my_name, my_last_name, my_age)
print(quote3)