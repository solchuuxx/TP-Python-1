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

num_positivo = 17
lista = []

def funcion(num_positivo):
    while num_positivo != 1:
            if num_positivo % 2 == 0:
                num_positivo = num_positivo // 2
                lista = [num_positivo]
                print(lista)
            else:
                num_positivo = num_positivo * 3 + 1
                lista = [num_positivo]
                print(lista)

funcion(num_positivo)
