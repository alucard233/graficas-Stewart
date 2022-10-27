#Capítulo 1
#Funciones lineales
#Página 34
#Ejercicio 21
#La tabla muestra la tasa de úlcera péptica (de por vida)(por cada 100 habitantes)
#en relación con el ingreso de varias familiares según lo informado por la
# Encuesta Nacional de Entrevista de Salud

from matplotlib import pyplot as plt
from matplotlib import interactive
from matplotlib import numpy as np
interactive(True)

xi = [4000, 6000, 8000, 12000, 16000, 20000, 30000, 45000, 60000]
yt = [14.1, 13.0, 13.4, 12.5, 12.0, 12.4, 10.5, 9.4, 8.2]

plt.plot(xi,yt)
plt.show

