## Funciones para calculos y Validaciones 
import csv 

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
            #Intenta una conversion si funciona convierte el valor a float
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
                #Intenta una conversion si funciona convierte el valor a int
                numero = int(dato)
                
                if numero <= 0:
                    print("Debes ingresar un numero entero mayor que 0.")
                else:
                    return numero
            except ValueError:
                print("Debes ingresar un numero entero valido.")
                
                
#Funcion para agregar producto. OPCION 1 MENU
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

#Funcion para mostrar inventario. OPCION 2 MENU
def mostrarInventario(productosTienda):
    print("\nINVENTARIO COMPLETO:")
    for clave in productosTienda:
        print("\nCodigo:", clave)
        print("Producto:", productosTienda[clave]["Producto"])
        print("Precio:", productosTienda[clave]["Precio"])
        print("Cantidad:", productosTienda[clave]["Cantidad"])

# Funcion para buscar en inventario OPCION 3 MENU
def buscarProducto(productosTienda):
    print("\nBUSCAR PRODUCTO")
    nombre_buscar = pedirNombre("Ingresa el nombre del producto a buscar: ")
    
    resultados = {
        clave: datos for clave, datos in productosTienda.items()
        if nombre_buscar.lower() in datos["Producto"].lower()
    }
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} producto(s):")
        for codigo, producto in resultados.items():
            print(f"\n  Código: {codigo}")
            print(f"  Producto: {producto['Producto']}")
            print(f"  Precio: ${producto['Precio']:,.2f}")
            print(f"  Cantidad: {producto['Cantidad']}")
    else:
        print(f"\nNo se encontraron productos con '{nombre_buscar}'")

#Funcion para actualizar producto OPCION 4 MENU
def actualizarProducto(productosTienda):
    print("\nACTUALIZAR PRODUCTO")
    nombre_actualizar = pedirNombre("Ingresa el nombre del producto a actualizar: ")
    
    print("\nDeja en blanco si no quieres modificar ese campo:")
    nuevo_precio = input("Nuevo precio (opcional): ").strip()
    nueva_cantidad = input("Nueva cantidad (opcional): ").strip()
    
    precio_convertido = None
    cantidad_convertida = None
    
    if nuevo_precio:
        try:
            precio_convertido = float(nuevo_precio)
            if precio_convertido <= 0:
                print("Precio inválido (debe ser mayor que 0)")
                precio_convertido = None
        except ValueError:
            print("Precio inválido, se omitirá la actualización de precio")
    
    if nueva_cantidad:
        try:
            cantidad_convertida = int(nueva_cantidad)
            if cantidad_convertida < 0:
                print("Cantidad inválida (no puede ser negativa)")
                cantidad_convertida = None
        except ValueError:
            print("Cantidad inválida, se omitirá la actualización de cantidad")
    
    actualizado = False
    for clave, datos in productosTienda.items():
        if datos["Producto"].lower() == nombre_actualizar.lower():
            if precio_convertido is not None:
                productosTienda[clave]["Precio"] = precio_convertido
            if cantidad_convertida is not None:
                productosTienda[clave]["Cantidad"] = cantidad_convertida
            actualizado = True
            break
    
    if actualizado:
        print(f"\nProducto '{nombre_actualizar.title()}' actualizado correctamente")
    else:
        print(f"\nNo se encontró el producto '{nombre_actualizar}'")


# Funcion para borrar producto OPCION 5 MENU
def eliminarProducto(productosTienda):
    print("\nELIMINAR PRODUCTO")
    clave = pedirEntero("Ingresa el codigo del producto a eliminar: ")
    
    if clave not in productosTienda:
        print("Codigo no encontrado.")
        return
    
    nombre = productosTienda[clave]["Producto"]
    confirmacion = input(f"¿Seguro que deseas eliminar '{nombre}'? (si/no): ").strip().lower()
    
    if confirmacion == "si":
        del productosTienda[clave]
        print(f"Producto '{nombre}' eliminado con éxito.")
    else:
        print("Operación cancelada.")
        

#Calcular estadisticas. OPCION 6 MENU 
def calcularEstadisticas(productosTienda):
    print("\nESTADISTICAS DEL INVENTARIO")
    print("1. Mostrar valor total del inventario")
    print("2. Cantidad total de productos registrados")
    print("3. Estadisticas detalladas")
    print("4. Regresar al menu principal")
    op = pedirOpcion(": ")

    if op == 1:
        total = 0
        for datos in productosTienda.values():
            total += datos["Precio"] * datos["Cantidad"]
        print(f"Valor total del inventario: ${total:,.2f}")

    elif op == 2:
        print(f"Productos registrados en inventario: {len(productosTienda)}")

    elif op == 3:
        if not productosTienda:
            print("No hay productos en el inventario.")
            return

        unidades_totales = 0
        valor_total = 0
        producto_mas_caro = None
        producto_mayor_stock = None
        precio_maximo = 0
        stock_maximo = 0

        for datos in productosTienda.values():
            unidades = datos["Cantidad"]
            precio = datos["Precio"]

            unidades_totales += unidades
            valor_total += precio * unidades

            if precio > precio_maximo:
                precio_maximo = precio
                producto_mas_caro = (datos["Producto"], precio)

            if unidades > stock_maximo:
                stock_maximo = unidades
                producto_mayor_stock = (datos["Producto"], unidades)

        
        print("ESTADISTICAS DETALLADAS")
        
        print(f"Unidades totales en stock: {unidades_totales}")
        print(f"Valor total del inventario: ${valor_total:,.2f}")

        if producto_mas_caro:
            nombre, precio = producto_mas_caro
            print(f"Producto mas caro: {nombre} - ${precio:,.2f}")
        else:
            print("Producto mas caro: No hay productos")

        if producto_mayor_stock:
            nombre, cantidad = producto_mayor_stock
            print(f"Producto con mayor stock: {nombre} - {cantidad} unidades")
        else:
            print("Producto con mayor stock: No hay productos")

    elif op == 4:
        return

    else:
        print("Opción no válida")


# Funcion guardar CSV. OPCION 7 MENU
def guardarCSV(productosTienda):
    import csv
    print("\nGUARDAR INVENTARIO")
    ruta = input("Nombre del archivo (Enter para 'inventario.csv'): ").strip()
    
    if not ruta:
        ruta = "inventario.csv"
    if not ruta.endswith(".csv"):
        ruta += ".csv"
    
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Codigo", "Producto", "Precio", "Cantidad"])
        for clave, datos in productosTienda.items():
            writer.writerow([clave, datos["Producto"], datos["Precio"], datos["Cantidad"]])
    
    print(f"Inventario guardado en '{ruta}' con éxito.")

# Funcion OPCION 8 MENU
def cargarCSV(productosTienda):
    import csv
    print("\nCARGAR INVENTARIO DESDE CSV")
    ruta = input("Ruta del archivo CSV: ").strip()
    
    if not ruta:
        print("Debes especificar una ruta de archivo.")
        return
    if not ruta.endswith(".csv"):
        ruta += ".csv"
    
    productos_cargados = []
    total_validos = 0
    invalidos = 0
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    productos_cargados.append({
                        "nombre": fila["Producto"],
                        "precio": float(fila["Precio"]),
                        "cantidad": int(fila["Cantidad"])
                    })
                    total_validos += 1
                except (ValueError, KeyError):
                    invalidos += 1
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta}'.")
        return
    
    print(f"\nResumen de carga:")
    print(f"  Productos válidos: {total_validos}")
    print(f"  Filas inválidas: {invalidos}")
    
    if total_validos == 0:
        return
    
    print("\n¿Cómo deseas cargar los datos?")
    print("S: Sobrescribir inventario actual")
    print("N: Fusionar con inventario actual")
    opcion_carga = input("Selecciona una opción (S/N): ").strip().upper()
    
    if opcion_carga == "S":
        productosTienda.clear()
        for i, producto in enumerate(productos_cargados, start=1):
            productosTienda[i] = {
                "Producto": producto["nombre"].title(),
                "Precio": producto["precio"],
                "Cantidad": producto["cantidad"]
            }
        print(f"\nInventario sobrescrito exitosamente. Total productos: {len(productosTienda)}")
    
    elif opcion_carga == "N":
        print("\nFusionando inventarios...")
        for producto in productos_cargados:
            encontrado = False
            for clave, datos in productosTienda.items():
                if datos["Producto"].lower() == producto["nombre"].lower():
                    productosTienda[clave]["Cantidad"] += producto["cantidad"]
                    if productosTienda[clave]["Precio"] != producto["precio"]:
                        productosTienda[clave]["Precio"] = producto["precio"]
                    encontrado = True
                    break
            if not encontrado:
                nuevo_codigo = max(productosTienda.keys()) + 1
                productosTienda[nuevo_codigo] = {
                    "Producto": producto["nombre"].title(),
                    "Precio": producto["precio"],
                    "Cantidad": producto["cantidad"]
                }
        print(f"\nInventario fusionado exitosamente. Total productos: {len(productosTienda)}")
    
    else:
        print("Opción no válida. Operación cancelada.")
    
    return len(productosTienda)