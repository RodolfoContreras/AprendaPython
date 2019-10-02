# Compara.py
# Autor: Contreras Galvan Rodolfo Alejandro
# Fecha de creación: 02/09/2019

n1=input("Introduce el numero 1: ")
n2=input("Introduce el numero 2: ")
R="Numeros propocionados: {} y {}. {}."

if n1==n2:
    print(R.format(n1,n2,"Los numeros son iguales"))
else:
    if n1>n2:
        print(R.format(n1,n2,"El numero mayor es el primero"))
    else:
        print(R.format(n1,n2,"El numero mayor es el segundo"))

