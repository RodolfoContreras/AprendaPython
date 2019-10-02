# Tabla.py
# Autor: Contreras Galvan Rodolfo Alejandro
# Fecha de creación: 02/09/2019

numero=int(input("Introduce un numero del 1 al 9: "))

for i in range(1,11):
    R="{} x {} = {}"
    print(R.format(numero,i,numero*i))