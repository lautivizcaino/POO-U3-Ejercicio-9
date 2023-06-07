import json
from listaVehiculos import ListaVehiculos

class Menu:
    __opcion:int
    def __init__(self) -> None:
        self.__opcion=int
    def opciones(self,jsonF,lista):
        while self.__opcion!=0:
            print('\n1 - Insertar Elemento\n2 - Agregar Elemento al Final\n3 - Mostrar Elemento\n4 - Modificar Precio de Usado\n5 - Mostrar vehiculo más económico\n6 - Mostrar Datos\n7 - Almacenar vehiculos en Archivo JSON\n0 - Salir')
            self.__opcion=int(input('Ingrese la opcion a ejecutar: '))
            if self.__opcion==1:
                print('\nOPCION 1')
                lista.insertarElemento()
            elif self.__opcion==2:
                print('\nOPCION 2')
                lista.agregarElementoFinal()
            elif self.__opcion==3:
                print('\nOPCION 3')
                lista.mostrarElemento()
            elif self.__opcion==4:
                print('\nOPCION 4')
                lista.mostrarPrecio()
            elif self.__opcion==5:
                print('\nOPCION 5')
                lista.mostrarEconomico()
            elif self.__opcion==6:
                print('\nOPCION 6')
                lista.mostrarDatos()
            elif self.__opcion==7:
                print('\nOPCION 7')
                lista.guardarVehiculos(jsonF)
        else:
            print('\nHA SALIDO DEL SISTEMA\n')