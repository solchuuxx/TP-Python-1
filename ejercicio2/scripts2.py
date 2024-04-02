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

'''
numero = int(input("Por favor, ingrese un número mayor que 1 y entero: "))
numeros = []

#Se forma la lista de los numeros
for i in range(1, numero + 1):
    numeros.append(i)

#Copia la lista completa antes de eliminar un numero
lista_completa = numeros.copy()

#Elimina un numero aleatorio de la lista
numero_eliminar = random.choice(numeros)
numeros.remove(numero_eliminar)

#Copia la lista incompleta, o sea, con el numero eliminado
lista_incompleta = numeros.copy()

#Se hace una resta de ambas listas para obtener el valor que falta
resultado = list(set(lista_completa) - set(lista_incompleta))
print(resultado[0], lista_incompleta)
'''

def missing_number(numero, numeros):
    lista_completa = list(range(1, numero + 1))
    lista_incompleta = numeros.copy()
    resultado = list(set(lista_completa) - set(lista_incompleta))
    return resultado[0]

numero = 5
numeros = [1, 2, 4, 5]
resultado = missing_number(numero, numeros)

print("Numero faltante: ", resultado)

assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
