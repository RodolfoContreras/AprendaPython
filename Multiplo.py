# Multiplo.py
# Autor: Contreras Galvan Rodolfo Alejandro
# Fecha de creación: 02/09/2019

#Simplifique el nombre de los multiplos

n=int(input("Introduce un numero entero: "))
m3=((n%3)==0)
m5=((n%5)==0)
m7=((n%7)==0)

if ((m3 and m5) or m7):
    print("Correcto")
else:
    print("Incorrecto")

