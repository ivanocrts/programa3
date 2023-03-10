"""
Programa 3. Autómata celular
Integrantes:
Cortés Alvarado Iván Daniel
Rodríguez Larios Alejandro 
Salgado Miranda Jorge

Desarrollar un código que muestre la evolución de un autómata celular unidimensional:
    * A partir de una población inicial aleatoria. 
    * Que genere el triángulo de Sierpinski.
"""

"""
Matplotlib: es una librería que permite generar gráficos a partir de los datos que se encuentran dentro 
de una lista o arreglo.
Numpy: es una librería que permite trabajar de manera fácil con arreglos, además de ofrecer herramientas útiles 
que apoyan el estudio y práctica de la ciencia de datos.

Para instalarlas y poder ejecutar el programa sin ningún problema es necesario abrir una terminal, en caso 
de Windows puede ser CMD o PowerShell. En cualquier caso basta con escribir las siguientes líneas de código:
    *numpy: pip install numpy
    *matplotlib: pip install matplot lib 

Los sitios web de las librerías son:
    *numpy: https://numpy.org/
    *matplotlib: https://matplotlib.org/stable/#
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng 

"""
La generación del triángulo de Sierpinski se basa en iteraciones. Las iteraciones en este programa hacen referencia 
a las veces en que se escoge un punto y se traza una línea.
"""
n = 2000000 #número de iteraciones

"""
En estos arreglos se almacenan las coordenadas de los puntos medios de las "líneas" que se generaron en el punto
anterior.
"""
#Arreglos donde guardamos las coordenadas de los puntos medios 
coordenadas_x = []
coordenadas_y = []

"""
Este punto puede tener cualquier ubicación. Posteriormente se "dirigirá" a cualquiera de los vértices y partir de
ahí comenzará la generación del triángulo de Sierpinski.
"""
#Punto de inicio
puntoInicio_x = 1
puntoInicio_y = 0.250

"""
Es necesario guardar la ubicación del primer punto en cada uno de los arreglos, es decir su ubicación en x y en y.
"""
#Ubicación del primer punto guardada en el arreglo
coordenadas_x.append(puntoInicio_x)
coordenadas_y.append(puntoInicio_y)

puntoMedio_x = 0
puntoMedio_y = 0

"""
Las siguientes líneas de código permiten ingresar las coordenadas de cada uno de los vértices del triángulo de Sierpinski;
el triángulo que se formará será equilátero. 
"""
#Coordenadas de los vértices
v1x = 0; v1y = 0
v2x = 4; v2y = np.sqrt(3)/2 #Altura de un triángulo equilatero. La función sqrt hace referencia a la raíz cuadrada y esta dentro de la librería numnpy.
v3x = 8; v3y = 0

"""
La creación del arreglo siguiente permite almacenar el número de iteraciones n que se estableció al inicio del código.
"""
r = []
r = rng(n)

"""
Este ciclo for permite elegir el verticé hacia el que se trazarán las líneas que formarán el triángulo de Sierpisnki.
"""
for i in range(n):
    if(r[i] < 1/3):
        verticex = v1x
        verticey = v1y
    elif (1/3 < r[i] < 2/3):
        verticex = v2x
        verticey = v2y
    elif (r[i]>2/3):
        verticex = v3x
        verticey = v3y
    #Cálculo del punto medio del primer punto.
    if(i==0):
        puntoMedio_x = (verticex+puntoInicio_x)/2
        puntoMedio_y = (verticey+puntoInicio_y)/2
    #Cálculo del punto medio de los demás puntos. 
    else:
        puntoMedio_x = (verticex+puntoMedio_x)/2
        puntoMedio_y = (verticey+puntoMedio_y)/2

    #Coordenadas de los puntos almacenadas en los arreglos coordenadas_x y coordenadas_y
    coordenadas_x.append(puntoMedio_x)
    coordenadas_y.append(puntoMedio_y)


plt.plot(coordenadas_x, coordenadas_y, 'b, ')
plt.text(0, 0.8, 'numero iteraciones = 2000000')
plt.show()

