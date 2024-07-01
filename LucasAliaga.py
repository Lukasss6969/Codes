import os
os.system("cls")

impresionMenuDatos="""
                                        DATOS DEL VEHICULO
-------------------------------------------------------------------------------------------------
MARCA        AÑO         KM          COSTO DEREPARACION          IMPUESTO            COSTO TOTAL
-------------------------------------------------------------------------------------------------
"""

buscadorVehiculo = f"""
          MENU OPCION
----------------------------------
1) TODO
2) BUSCAR POR MARCA
----------------------------------
SELECCIONE UNA OPCION: """

menuPrincipal="""
            MENU PRINCIPAL
------------------------------------------
1) REGISTRAR VEHICULO
2) LISTAR TODOS LOS VEHICULOS REGISTRADOS
3) IMPRIMIR ORDEN DE REPARACION
4) SALIR
------------------------------------------
SELECCIONE UNA OPCION: """

ordenVehiculo=[]

def registrarVehiculo():
    marcaVehiculo=input("INGRESE LA MARCA DEL VEHICULO: ").upper()
    añoDeFabricacion=int(input("INGRESE EL AÑO DE FABRICACION DEL VEHICULO: "))
    kilometraje=int(input("INGRESE EL KILOMETRAJE DEL VEHICULO: "))
    costodeReparacionEstimado=int(input("INGRESE LOS COSTOS DE REPARACION DEL VEHICULO (EN PESOS): "))
    impuestoCostoReparacion = costodeReparacionEstimado*0.08
    costoTotal = impuestoCostoReparacion + costodeReparacionEstimado
    ordenVehiculo.append([marcaVehiculo, añoDeFabricacion, kilometraje, costodeReparacionEstimado, round(impuestoCostoReparacion), round(costoTotal)])


def listarVehiculosRegistrados():
    salida=impresionMenuDatos
    for menu in ordenVehiculo:
        salida += f"{menu[0]:<13}"
        salida += f"{menu[1]:<12}"
        salida += f"{menu[2]:<10}"
        salida += f"{menu[3]:>12}"
        salida += f"{menu[4]:>24}"
        salida += f"{menu[5]:>24}"
        salida +="\n"
    return salida

def imprimirOrdendeReparacion():
    opcImprimir=int(input(buscadorVehiculo))
    if opcImprimir == 1:
        nombreArchivo=input("INGRESE EL TITULO DEL ARCHIVO: ")
        with open(f"{nombreArchivo}" + ".txt", "w") as archivo:
            archivo.write(listarVehiculosRegistrados())
    elif opcImprimir == 2:
        marcaVehiculoaBuscar=input("INGRESE LA MARCA DEL VEHICULO QUE DESEA BUSCAR: ").upper()
        nombreArchivo=input("INGRESE EL TITULO DEL ARCHIVO: ")
        with open(f"{nombreArchivo}" + ".txt", "w") as archivo:
            if ordenVehiculo.index(marcaVehiculoaBuscar):
                archivo.write(listarVehiculosRegistrados())
            else:
                input("MARCA NO ENCONTRADA | INTENTE NUEVAMENTE")
    else:
        input("ERROR EN RANGO DE DATOS INGRESADOS | 'ENTER' PARA CONTINUAR")
while True:
  os.system("cls")
    try:
        opcMenuPrincipal=int(input(menuPrincipal))
        if opcMenuPrincipal == 1:
            registrarVehiculo()
        elif opcMenuPrincipal == 2:
            print(listarVehiculosRegistrados())
        elif opcMenuPrincipal == 3:
            imprimirOrdendeReparacion()
        elif opcMenuPrincipal == 4:
            break
        else:
            input("ERROR EN RANGO DE DATOS INGRESADOS | 'ENTER' PARA CONTINUAR")
    except:
        input("ERROR EN LA EXCEPCION DE MENU PRINCIPAL | 'ENTER' PARA CONTINUAR")
