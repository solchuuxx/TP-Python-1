'''
Ejercicio 2: “Missing Number”
Se te dan todos los números entre 1 a “n” excepto uno. Tu tarea es encontrar el número que
falta.

Input:
El primer parámetro contiene la cantidad de elementos del array.
El segundo parámetro contiene “n” números. Cada número es único y está entre 1 y n
(inclusive).
Output:
Retornar el número que falta.
Caso de prueba:
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de
prueba"
'''
import random

numero = int(input("Por favor, ingrese un número mayor que 1 y entero: "))
numeros = []

for i in range(1, numero + 1):
    numeros.append(i)

lista_completa = numeros.copy()

numero_eliminar = random.choice(numeros)
numeros.remove(numero_eliminar)

lista_incompleta = numeros.copy()

resultado = list(set(lista_completa) - set(lista_incompleta))
print("El número faltante es:", resultado[0] , " Lista: " , (lista_incompleta))