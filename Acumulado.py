# Acumulado.py
# Autor: Contreras Galvan Rodolfo Alejandro
# Fecha de creación: 02/09/2019

i=int(0)
numero=str("")

while True:
    numero=input("Introduce un numero entero: ")
    if numero=="":
        print("Vacio, salida del programa")
        break
    else:
        i+=int(numero)
        salida="Cantidad acumulada: {}"
        print(salida.format(i))