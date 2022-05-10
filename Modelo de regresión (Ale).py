from audioop import add
from cmath import sqrt
from statistics import mean
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
from sympy import Add
#Y=mx+b
# Datos de una empresa que remodela casas viejas en Manhattan 
K= 4
X= [1,3,4,2,1,7]
Y= [2,3,2.5,2,2,3.5]
n= len(X)                             #Contar cuantos datos hay en X
Z= np.array(X)*np.array(Y)            #XY
F= (np.array(X))**2
G= (np.array(Y))**2

#Hallar la pendiente del modelo 
m= (sum(Z)-(n*(mean(Y))*(mean(X))))/((sum((np.array(X))**2))-n*(mean(X))**2)
print("La pendiente es:",m)

#Hallar la ordenada
b= (mean(Y)-m*(mean(X)))
print("El intercepto es:", b)

#Ecuación de la recta 
print("La ecuación de la recta es") 
print(b,"+",m,"X")

#Cuando nos dan el valor de x hallar cuanto es Y
x= 6
print("Tomando el valor dado de X, Y es:", (np.round(b+m*x)))

#Gráfica
plt.plot((0,x), (b,(b+m*x)), label='Línea de regresión', color = "m")
plt.scatter(X,Y,c="blue", marker=".") #Diagrama de dispersión color ponerle ycomo desea que esten los puntos 
plt.xlabel("Nómina")                  #Nombrar el eje x
plt.ylabel("Ventas")                  #Nombrar el eje Y
plt.title("Regresión Líneal")         #Título del Gráfico
plt.show()

#Error estandar de la estimación
S= sqrt((((sum((np.array(Y))**2))-b*sum(Y)-m*sum(Z))/4))
print("El error estándar de la estimación es:",(np.round(S,K)))

#Coeficienes de correlación para rectas de Regresión 
#r= 1 correlación positiva perfecta
#0<r<1  Correlación positiva
#r=0 no hay correlación
#r=-1 correlación negativa perfecta 
r= (n*sum(Z)-sum(X)*sum(Y))/sqrt((n*sum(F)-(sum(X))**2)*(n*sum(G)-(sum(Y)**2)))
print("El coeficiente de correlación es:", (np.round(r,K)))

#Coeficiente de determinación
#Porcentaje de variación en la variable dependiente (y) que explica la ecuación de regresión 
#Qué tan exacto es el modelo
D= r**2
print("El coeficiente de determinación es:", (np.round(D,K)))