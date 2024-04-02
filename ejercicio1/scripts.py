'''Ejercicio 1: “Weird Algorithm”
Considera un algoritmo que toma como entrada un entero positivo n. Si n es par, el algoritmo
lo divide por dos, y si n es impar, el algoritmo lo multiplica por tres y le suma uno. El
algoritmo repite esto hasta que n sea uno. Por ejemplo, la secuencia para el valor 3 es la
siguiente:
3 ➝ 10 ➝ 5 ➝ 16 ➝ 8 ➝ 4 ➝ 2 ➝ 1
Tu tarea es simular la ejecución del algoritmo para un valor dado de n.
Input:
La única línea de entrada contiene un entero n.
Output:
Imprime una línea que contenga todos los valores de n durante la ejecución del algoritmo.
Constraints:
1 < n < 10
6

Caso de prueba:
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en
el caso de prueba"'''

num_positivo = 0
lista = []

def weird_algorithm(num_positivo):
    lista = [num_positivo]
    actual = num_positivo   #Almacena el valor actual
    while actual != 1:
        if actual % 2 == 0:
            actual = actual // 2
        else:
            actual = actual * 3 + 1
        lista.append(actual)  #agrega el valor actual a la lista
    return lista

#weird_algorithm(num_positivo)
resultado = weird_algorithm(3)
print(resultado)

# Test
assert resultado == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
#El codigo se ejecuta y finaliza correctamente ya que no hay ningun error.