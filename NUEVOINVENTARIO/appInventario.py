from serviciosInventario import pedirOpcion, agregarProducto,mostrarInventario, calcularEstadisticas


## Listado de inventarios productos 

productosTienda = { 
    1: {"Producto": "Resma de Papel", "Precio": 7000, "Cantidad": 100},
    2: {"Producto": "Lapicero Negro", "Precio": 1500, "Cantidad": 100},
    3: {"Producto": "Lapicero Rojo", "Precio": 1200, "Cantidad": 100},
    4: {"Producto": "Pincel", "Precio": 1000, "Cantidad": 100}
    }


inventario = "Si"
agregar = "si"


## EJECUCION DEL INVENTARIO

inventario = False
contador = len(productosTienda)

while inventario == False:
        print ("\nINVENTARIO TIENDA")
        print ("1. Agregar producto")
        print ("2. Mostrar Inventario") 
        print ("3. Calcular Estadisticas")
        print ("4. Salir")
        
        opcion = pedirOpcion("Escoge una opción: ")
            
        if opcion == 1:
            contador = agregarProducto(productosTienda, contador)
                 
        elif opcion == 2:
            mostrarInventario(productosTienda)
        elif opcion == 3:
            calcularEstadisticas(productosTienda)
        elif opcion == 4:
            inventario = True
            print ("Cerrando Inventario")
        else:
            print ("opcion no valida")


            
