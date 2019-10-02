# Aleatorio.py
# Autor: Contreras Galvan Rodolfo Alejandro
# Fecha de creación: 02/09/2019

#Se importan librerias
import random

#Quise pedir la variable al usuario
numero1=float(input("Introduce un numero del tipo float: "))


def aleatorio():
    numero2=float(random.randrange(1,10))
    R="la suma del numero introducido: {}, y el numero aleatorio: {}, es {}"
    print(R.format(numero1,numero2,numero1+numero2))

aleatorio()