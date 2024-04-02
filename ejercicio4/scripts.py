'''
Ejercicio 4: “Palindrome Reorder”
Dada una cadena de caracteres, tu tarea es reorganizar los caracteres de la cadena de manera
que puedas formar un palíndromo. Si no es posible formar un palíndromo, debes indicarlo.
Input:
El único parámetro contiene una cadena de caracteres de longitud n ( 1 ≤ n ≤ 10^6 ). La
cadena solo contiene letras minúsculas del alfabeto inglés.
Output:
Retorna una cadena que represente un palíndromo formado reorganizando los caracteres de la
cadena de entrada. Si no es posible formar un palíndromo, retorna "NO SOLUTION".
Caso de prueba:
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso
de prueba"
'''
from collections import Counter

while True:
    #cadena = str(input("Ingrese una cadena de caracteres: "))
    cadena = "aabbc"
    if len(cadena) >= 1 and len(cadena) <= 10**2 and cadena.islower() and cadena.isalpha():
        break
    else:
        print("Ingresa caracteres válidos por favor: ")

def palindrome_reorder(cadena):
    #cuenta la frecuencia de cada caracter
    frecuencia = Counter(cadena)

    #Verifica si se puede formar un palindromo, y sino, retorna una oración
    caract_cont = sum(count % 2 for count in frecuencia.values())
    if caract_cont > 1:
        return "No hay solución para formar el palíndromo"

    #Construye la primer mitad del palindromo
    mitad_palin = [char * (count // 2) for char, count in frecuencia.items()]
    mitad_segun_palin = mitad_palin.copy()

    #Si hay un caracter impar, lo añade al medio (aabbc = c = ab C ba)
    caract_lista = [char for char, count in frecuencia.items() if count % 2]
    mitad_palin.append(caract_lista[0] if caract_lista else '')

    #Construye el palindromo entero, uniendo la primer mitad del palindromo y la segunda mitad del mismo.
    palindromo = ''.join(mitad_palin + mitad_segun_palin[::-1])

    return palindromo

#resultado = reordenar_palindromo(cadena)
print("Palindromo: ", palindrome_reorder(cadena))
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
