"""
Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.

La función multiply_numbers recibirá como entrada una lista con números. Finalmente, la función retornará la lista transformada.

Ejemplo 1:

Input: [2, 4, 5, 6, 8]
Output: [4, 8, 10, 12, 16]

Ejemplo 2:

Input: [1, 1, -2, -3]
Output: [1, 1, -4, -6]
"""
def multiply_numbers(numbers):
    # Escribe tu solución 👇    
    resultado = list(map(lambda numeros: numeros * 2, numbers))
    resultado2 = list(map(lambda numeros: numeros * 2, Input))
    return resultado, resultado2

numbers = [1, 2, 3, 4]
Input = [1, 1, -2, -3]
resultado = multiply_numbers(numbers)
print("========")
resultado2 = multiply_numbers(numbers)
print(resultado2)