#Examen Parcial
#Autor: Rodolfo Alejandro Contreras Galvan
#Matricula: 1818772
#Grupo: 22

import os
import time
vendedor={}  
venta={} 
salir=1 
s=0 

opciones=(1,2,3,4,5,"1","2","3","4","5")
uno=(1,"1")
dos=(2,"2")
tres=(3,"3")
cuatro=(4,"4")
cinco=(5,"5")



while salir==1: 

 
    print("Menu\n\n1) Registrar un vendedor\n2) Registrar una venta\n3) Consultar el listado de vendedores\n4) Reportar las ventas capturadas\n5) Salir\n") 
    opcion=input("Elige una opcion: ")
    
    
    
    if opcion in opciones: 

 

        if opcion in uno: 

            print("Seleccionaste regist1rar un vendedor\n") 
            clave=int(input("Ingresa una clave (numero entero): ")) 

            if clave not in vendedor: 

                vendedor[clave]=input("Ingresa apellidos y nombre: ") 
                print("Vendedor registrado\n")
                time.sleep(5)
                os.system("clear")

            else: print("La clave ya existe\n") 
            time.sleep(2)
            os.system("clear")


                
 

        if opcion in dos: 

            print("Seleccionaste registrar una venta\n") 
            a=int(input("Ingresa la clave de un vendedor: ")) 

            if a in vendedor: 

                f=int(input("Ingresa un folio: ")) 

                if f not in venta: 

                    m=int(input("Ingresa monto: ")) 
                    venta[f]=m 
                    s=s+m 
                    m=0 
                    print("Venta registrada\n") 
                    time.sleep(2)
                    os.system("clear")

                else: print("El folio ya existe")
                time.sleep(5)
                os.system("clear") 

            else: 

                print("No hay ningun vendedor con esa clave") 
            time.sleep(5)
            os.system("clear")
            
 

        if opcion in tres: 

            print("Seleccionaste mostrar los vendedores registrados\n") 
            print("La clave y vendedor son: ") 

            for key in vendedor: 
            
                    print("Clave:", key, "Nombre:", vendedor[key])
                    print(" ")
            time.sleep(5)
            os.system("clear")
 

 

        if opcion in cuatro: 

            print("Seleccionaste mostrar las ventas registradas\n") 
            print("El folio y monto de la venta son: ") 

            for key in venta: 

                print ("Folio:", key, "Monto:", venta[key]) 
                
                
            print("La suma total de los montos es: ", s) 
            print("\n") 
            time.sleep(5)
            os.system("clear")
 

 

        if opcion in cinco: 

            
           
            print("Saliste")
            salir=2

 

    else: 

         print("introduce una opcion valida\n")
         time.sleep(5)
         os.system("clear") 