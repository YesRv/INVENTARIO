## Funciones para calculos y Validaciones 


#Pedir opcion 
def pedirOpcion(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato == "":
            print("No puedes dejar el campo vacio.")
        elif "." in dato or "," in dato:
            print("Ingresar un numero entero, sin puntos ni comas.")
        #sirve para verificar si una cadena de texto (string) contiene exclusivamente caracteres numéricos (dígitos del 0 al 9)
        elif dato.isdigit():
            return int(dato)
        else:
            print("Entrada no valida. Debes ingresar solo numeros enteros.")


#Funcion para pedir el nombre de cada producto
def pedirNombre(mensaje):
    while True:
        texto = input(mensaje).strip()
        
        if texto == "":
            print("Este campo no puede estar vacío.")
        #revisa si *algún* carácter del texto es un dígito, que es lo que realmente quieres validar.
        elif any(ch.isdigit() for ch in texto):
            print("Por favor ingresa un nombre válido, sin números.")
        else:
            return texto.lower().title()
        
#Funcion para pedir el precio de cada producto        
def pedirPrecio(mensaje):
    while True:
        dato = input(mensaje).strip()
        
        if dato == "":
            print("Este campo no puede estar vacio.")
        else:
            try:
                numero = float(dato)
                
                if numero <= 0:
                    print("Valor menor que 0. Error")
                else:
                    return numero
            except ValueError:
                print("Valor no valido. Error")

#Funcion para pedir la cantidad de cada producto
def pedirEntero(mensaje):
    while True:
        dato = input(mensaje).strip()
        
        if dato == "":
            print("Este campo no puede estar vacio.")
        else:
            try:
                numero = int(dato)
                
                if numero <= 0:
                    print("Debes ingresar un numero entero mayor que 0.")
                else:
                    return numero
            except ValueError:
                print("Debes ingresar un numero entero valido.")
                
                
#Funcion para agregar producto
def agregarProducto(productosTienda, contador):
    while True:
        print ("1. Agregar productos al inventario")
        print ("2. Regresar al menu principal")
        op = pedirOpcion (": ")
        if op == 1:
            contador += 1
                    
            nombreProducto = pedirNombre("Producto: ")
            precioProducto = pedirPrecio("Precio: ")
            cantidadProducto = pedirEntero("Cantidad: ")
            #Diccionario para agregar un nuevo producto al inventario                
            nuevoProducto = { "Producto": nombreProducto,
                                "Precio": precioProducto,
                                "Cantidad":cantidadProducto,
                            }
            productosTienda [contador]= nuevoProducto 
            print (f"Producto {nombreProducto} agregado con exito: ")
        elif op == 2:
            break
        else:
            print("Opcion no valida")   
    return contador

#Funcion para mostrar inventario 
def mostrarInventario(productosTienda):
    print("\nINVENTARIO COMPLETO:")
    for clave in productosTienda:
        print("\nCodigo:", clave)
        print("Producto:", productosTienda[clave]["Producto"])
        print("Precio:", productosTienda[clave]["Precio"])
        print("Cantidad:", productosTienda[clave]["Cantidad"])

#Calcular estadisticas
def calcularEstadisticas(productosTienda):
    print ("1. Mostrar valor total del inventario")
    print("2. Cantidad Total de productos registrados")
    print ("3. Regresar al menu principal")
    op = pedirOpcion (": ")
    total = 0
    if op == 1:
        #Ciclo que recorre todos mis productos 
        for clave in productosTienda.values():
            #Llamo el valor con el nombre de la clave
            total += clave["Precio"] * clave["Cantidad"]
        #total:,.2f en el f-string sirve para formatear el número con separador de miles y mostrar decimales
            print(f"Valor total del inventario: ${total:,.2f}")
    elif op == 2:
            print(f" Productos registrados en Inventario:  {len(productosTienda)}")
    elif op == 3:
            return
    else:
            print("Opción no valida") 