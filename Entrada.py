# Entrada.py
# Autor: Contreras Galvan Rodolfo Alejandro
# Fecha de creación: 02/09/2019

valor=input("Introduce un valor: ")
print(type(valor))
entero=(valor.isdigit() and valor.find(".")==-1)

#Hice un ciclo para poder introducir nuevamente los datos si la condición es falsa

while entero is False:
    print("El dato no es entero, intenta nuevamente")
    valor=input("Introduce un valor: ")
    print(type(valor))
    entero=(valor.isdigit() and valor.find(".")==-1)
else:
    print("El dato introducido es entero, Muy bien!")
