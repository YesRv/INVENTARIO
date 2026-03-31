from serviciosInventario import pedirOpcion, agregarProducto,mostrarInventario, calcularEstadisticas, eliminarProducto 
from serviciosInventario import buscarProducto, actualizarProducto, guardarCSV, cargarCSV


## Listado de inventarios productos 

productosTienda = {}


inventario = "Si"
agregar = "si"


## EJECUCION DEL INVENTARIO

inventario = False
contador = len(productosTienda)

while inventario == False:
    print ("\nINVENTARIO TIENDA")
    print ("1. Agregar producto")
    print ("2. Mostrar Inventario")
    print ("3. Buscar en Inventario") 
    print ("4. Actualizar Inventario") 
    print ("5. Eliminar dato de Inventario") 
    print ("6. Calcular Estadisticas")
    print ("7. Guardar CSV")  
    print ("8. Cargar CSV")  
    print ("9. Salir")
        
    opcion = pedirOpcion("Escoge una opción: ")
            
    if opcion == 1:
        contador = agregarProducto(productosTienda, contador)
                 
    elif opcion == 2:
        mostrarInventario(productosTienda)     
    elif opcion == 3:
        buscarProducto(productosTienda)
    elif opcion == 4:
        actualizarProducto(productosTienda)
    elif opcion == 5:
        eliminarProducto(productosTienda)
    elif opcion == 6:
        calcularEstadisticas(productosTienda)
    elif opcion == 7:
        guardarCSV(productosTienda)
    elif opcion == 8:
        resultado = cargarCSV(productosTienda)
        if resultado:
            contador = resultado       
    elif opcion == 9:
        inventario = True
        print ("Cerrando Inventario")
    else:
        print ("opcion no valida")

