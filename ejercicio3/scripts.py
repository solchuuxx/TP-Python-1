'''
Ejercicio 3: “Number Spiral”
Un espiral numérico es una cuadrícula infinita cuyo cuadrado superior izquierdo tiene el
número 1. Aquí están las primeras cinco capas del espiral.

Tu tarea es descubrir el número en la fila x y la columna y.
Input:
El primer parámetro contiene la posición de la fila de la matriz espiral
El segundo parámetro contiene la posición de la columna de la matriz espiral
Output:
Retornar el valor de la matriz en la posición seleccionada.
Caso de prueba:
assert number_spiral(2, 2) == 25, "Error en el caso de
prueba"
'''
matriz = [[1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]

def spiral(m):
 a=[]
 t=list(zip(*m)) # Obtienes las columnas por la función zip

 while m!=[]:
  if m==[]:
    break
  m=list(zip(*t)) # zip t te dará la misma matriz m. Es necesario para la iteración
  a.extend(m.pop(0)) # Paso 1 : abre la primera fila
  if m==[]:
    break
  t=list(zip(*m))
  a.extend(t.pop(-1)) # Paso 2: saca la última columna
  if m==[]:
    break
  m=list(zip(*t))
  a.extend(m.pop(-1)[::-1]) # Paso 3: coloca la última fila en orden inverso
  if m==[]:
    break
  t=list(zip(*m)) 
  a.extend(t.pop(0)[::-1]) # Paso 4: coloca la primera columna en orden inverso
 return a

def obtener_valor(x, y):
    if x > y:
        if x % 2 == 0:
            return x * x - y + 1
        else:
            return (x - 1) * (x - 1) + y
    else:
        if y % 2 == 0:
            return (y - 1) * (y - 1) + x
        else:
            return y * y - x + 1


espiral = spiral(matriz)
#valor = obtener_valor(1,4) #(fila,columna)
#print(valor)

assert obtener_valor(2, 2) == 3, "Error en el caso de prueba"