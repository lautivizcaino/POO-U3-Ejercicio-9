from zope.interface import implementer
import json
from vehiculo import Vehiculo
from interfaces import Interfaz
from nodo import Nodo
from nuevo import Nuevo
from usado import Usado
@implementer(Interfaz)
class ListaVehiculos:
    __comienzo:None
    __cantidad:int
    def __init__(self) -> None:
        self.__comienzo=None
        self.__cantidad=0

    def toJSON(self): 
        d = dict(
            __class__=self.__class__.__name__,
            vehiculos=[] 
            ) 
        aux=self.__comienzo
        while aux!=None:
            vehiculo=aux.getVehiculo()
            d['vehiculos'].append(vehiculo.toJSON())
            aux=aux.getSiguiente()
        return d
    
    def agregarVehiculo(self,vehiculo):
        nodo=Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__cantidad+=1
    
    def mostrarLista(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getVehiculo())
            aux=aux.getSiguiente()

    def crearElemento(self):
            tipo=int(input('Ingrese tipo de vehiculo (1 - Nuevo/2 - Usado): '))
            marca=input('Ingrese marca: ')
            modelo=input('Ingrese modelo: ')
            puertas=int(input('Ingrese puertas: '))
            color=input('Ingrese color: ')
            precio=float(input('Ingrese precio: '))
            if tipo==1:
                version=input('Ingrese version: ')
                unNuevo=Nuevo(marca,modelo,puertas,color,precio,version)
                nodo=Nodo(unNuevo)
            elif tipo==2:
                patente=input('Ingrese patente: ')
                año=int(input('Ingrese año: '))
                km=int(input('Ingrese kilometraje: '))
                unUsado=Usado(marca,modelo,puertas,color,precio,patente,año,km)
                nodo=Nodo(unUsado)
            return nodo


    def insertarElemento(self,posicion,vehiculo):
        if posicion>=0 and posicion<=self.__cantidad:
            nodo=Nodo(vehiculo)
            if nodo!=None:
                contador=0
                if posicion==0:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__cantidad+=1
                else:
                    post=self.__comienzo
                    ant=self.__comienzo
                    while post!=None and posicion>contador:
                        ant=post
                        post=post.getSiguiente()
                        contador+=1
                    if posicion==contador:
                        ant.setSiguiente(nodo)
                        nodo.setSiguiente(post)
                        self.__cantidad+=1

    def agregarElementoFinal(self,vehiculo):
        nodo=Nodo(vehiculo)
        if nodo!=None:
            if self.__comienzo==None:
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__cantidad+=1
            else:
                post=self.__comienzo
                while post!=None:
                    ant=post
                    post=post.getSiguiente()
                ant.setSiguiente(nodo)
                self.__cantidad+=1


    def mostrarElemento(self,posicion):
        if posicion>=0 and posicion<=self.__cantidad:
            contador=0
            if posicion==0:
                vehiculo=self.__comienzo.getVehiculo()
            else:
                aux=self.__comienzo
                while aux!=None and posicion>contador:
                    aux=aux.getSiguiente()
                    contador+=1
                if posicion==contador:
                    self.__cantidad+=1
                    vehiculo=aux.getVehiculo()
            return vehiculo
                    

    def mostrarPrecio(self,patente,precio):
        aux=self.__comienzo
        encontrado=False
        while aux!=None and not encontrado:
            if isinstance(aux.getVehiculo(),Usado):
                unUsado=aux.getVehiculo()
                if unUsado.getPatente()==patente:
                    unUsado.setPrecio(precio)
                    encontrado=True
                    print('Precio de venta:%.2f'%(unUsado.getVenta()))
            aux=aux.getSiguiente()
        if not encontrado:
            print('No existe un vehiculo con la patente ingresada')
        return unUsado.getVenta()

    def mostrarEconomico(self):
        aux=self.__comienzo
        unVehiculo=aux.getVehiculo()
        min=unVehiculo.getVenta()
        while aux!=None:
            unVehiculo=aux.getVehiculo()
            if unVehiculo.getVenta()<min:
                min=unVehiculo.getVenta()
            aux=aux.getSiguiente()
        aux=self.__comienzo
        while aux!=None:
            unVehiculo=aux.getVehiculo()
            if unVehiculo.getVenta()==min:
                print('%s Importe de Venta:%.2f'%(unVehiculo,unVehiculo.getVenta()))
            aux=aux.getSiguiente()
    
    def mostrarDatos(self):
        aux=self.__comienzo
        while aux!=None:
            unVehiculo=aux.getVehiculo()
            print('Modelo:%s Cantidad de puertas:%d Importe de venta:%.2f'%(unVehiculo.getModelo(),unVehiculo.getPuertas(),unVehiculo.getVenta()))
            aux=aux.getSiguiente()
    
    def guardarVehiculos(self,jsonF):
        d=self.toJSON()
        jsonF.guardarJSONArchivo(d,'vehiculos.json')
        print('\nArchivo guardado con éxito')
    
    def getNombres(self):
        aux=self.__comienzo
        modelos=[]
        while aux!=None:
            vehiculo=aux.getVehiculo()
            modelos.append(vehiculo.getModelo())
            aux=aux.getSiguiente()
        return modelos
