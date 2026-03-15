## Inventario de Tienda

## Tarea 2

inventario = "si" 

## Bucle que se cumplira siempre que quiera ingresar datos al inventario
while inventario == "si":
    ##Menú para guiar mi acceso al inventario
    print ("INVENTARIO TIENDA")
    print ("1. Ingresar datos al inventario")
    print ("2. Salir")
    ##Variable que me permite seleccionar los datos del menú
    opcion = input("Elige una opción: ")

    ## Condición para ingresar datos
    if opcion == "1":

        nombre = str(input("Ingresa el nombre del producto: "))
        ##Mientras ingresemos un nombre para el producto el programa va a ejecutar el ciclo para validar Precio y Cantidad
        while True:
            ### Validación de Precio (El try Le dice a Python: "Intenta convertir esto a número" )
            try:
                precio = float (input("Ingresa el precio del producto: "))
                if precio < 0:
                    print ("Valor no valido")
                else:
                    ## Si la conversión de float() o int() funciona correctamente, el código llega a la línea del break y 
                    # escapa del ciclo para pasar al siguiente dato
                    break
            ##Aquí, el except atrapa el error, imprime el mensaje de error personalizado y evita que el programa termine.    
            except ValueError:
                print("Ingresa un número decimal valido")

            ##Validacion de Cantidad (Seguiria las mismas condiciones de precio)     
        while True:
            try:
                cantidad = int (input("Ingresa la cantidad del producto: "))
                if cantidad < 0:
                    print ("Valor no valido")
                else:
                    break # Sale solo de este bucle si la cantidad es correcta
            except ValueError:
                ("Ingresa un valor valido")
        ## Para validar los datos ingreados procedemos a realizar la operacion con el calculo
        ## Si se cumplen las condiciones el programa debera mostrar el total de los datos ingresados
        total = precio * cantidad
        print ("Articulo: ", nombre)
        print ("Precio und: ", precio)
        print ("Cantidad: ", cantidad," und")
        print ("Total: ", total)
    ## Opcion para terminar el menu de ingreso de articulos
    elif opcion == "2": 
        print ("inventario Terminado")
        inventario = "no"
    else:
        print("Valor no valido")

## Instruccion para terminar el programa o continuar con el ingreso de mas productos 
seguir = input("¿Desea ingresar otro producto? (si/no): ")

