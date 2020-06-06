#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios con bucles "while"

    x = 0
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración
    condicion = 6
    while x < condicion:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        # Coloque la línea de código para que "X" incremente "1"
        x += 1
        
    x = 5
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    while x >= 0:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        # Coloque la línea de código para que "X" decremente "1"
        x -= 1
        

def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = ['rojo', 'naranja', 'verde', 'azul']
    
    for i in colores:
        print(i)
    
    
    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...
    for color in colores:
        print(color)
    
   
    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...
    
    colores_len = len(colores)

    for i in range(colores_len):
        print (" color: {}".format(colores[i]))

def ej3():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero
   #metodo 1
    numero_len = len(numeros)
    
    for i in range (numero_len):
        
        suma +=  numeros[i] 
        
        continue
        
    print("La suma es: {}".format(suma))
   #metodo 2
    sumatoria = 0
    for i in numeros:
        sumatoria += i
        
    print("LA SUMA METODO 2 ES {}".format(sumatoria))


        


def ej4():
    # Ejercicios con bucles "while"

    x = 0
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    while x < 10 and x != 6:
        print("El valor de x es : {}".format(x))
        x += 2
        continue

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    x = 0
    while x < 10:
        if x == 6:
            print("x es igual a 6")
        else:
            print("El numero de x es: {}".format(x))

        x +=2
     


     



def ej5():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    
    # fin....
    fin = int(input("Ingrese el numero final de la secuencia\n" ))

    # for ... in range(....)
    suma = 0
    for i in range(inicio,fin):
        suma += i
        
    print("La suma de la secuencia de numeros del inicio hasta el numero anterior al fin es de: {}".format(suma))




    # Imprimir el valor de la sumatoria


def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    # fin....
    fin = int(input("Ingrese el ultimo numero de la secuencia\n"))


    cantidad_numeros_positivos = 0  # Inicializo el contador en 0
    #cantidad_numeros_negativos
    cantidad_numeros_negativos = 0

    # for ... in range(....)
    for i in range(inicio,fin):
        if i < 0:
            cantidad_numeros_negativos += 1
        elif i >= 0:
            cantidad_numeros_positivos +=1
    print("Cantidad de numeros negativos: {}".format(cantidad_numeros_negativos))
    print("Cantidad de numeros positivos: {}".format(cantidad_numeros_positivos))
        

    # Imprimir el valor de la cantidad de números positivos y negativos


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    #ej6()
