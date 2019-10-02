# Tablas.py
# Autor: Contreras Galvan Rodolfo Alejandro
# Fecha de creación: 02/09/2019


for tabla in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(tabla))
    print()
    for tablas in range(1,11):
        R="{} x {} = {}"
        print(R.format(tabla,tablas,tabla*tablas))
    else:
        print()