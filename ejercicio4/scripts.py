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

while True:
    cadena = str(input("Ingrese una cadena de caracteres: "))
    if len(cadena) >= 1 & len(cadena) <= 10**2 & cadena.islower() & cadena.isalpha():
        break
    else:
        print("Ingresa caracteres válidos por favor: ")

def es_palindromo(cadena):
    if cadena == cadena[::-1]:
        return ("Es palindromo: ", cadena)
    else: 
        return ("No es palindromo")

resultado = es_palindromo(cadena)
print(resultado)
