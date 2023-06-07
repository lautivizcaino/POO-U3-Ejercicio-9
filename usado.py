from vehiculo import Vehiculo
from datetime import datetime
class Usado(Vehiculo):
    __patente:str
    __anio:int
    __km:int
    def __init__(self, marca, modelo, cantidadPuertas, color, precioBase,patente,anio,km) -> None:
        super().__init__(marca, modelo, cantidadPuertas, color, precioBase)
        self.__patente=patente
        self.__anio=anio
        self.__km=km
    def __str__(self) -> str:
        return super().__str__() + 'Patente:%s Año:%s Kilometraje:%s'%(self.__patente,self.__anio,self.__km)
    
    def getPatente(self):
        return self.__patente
    def getVenta(self):
        importe=self.getPrecio()-self.getPrecio()*(datetime.now().year-self.__anio)*0.01
        if self.__km>100000:
            importe-=self.getPrecio()*0.02
        return importe
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getMarca(),
                modelo=self.getModelo(),
                cantidadPuertas=self.getPuertas(),
                color=self.getColor(),
                precioBase=self.getPrecio(),
                patente=self.__patente,
                anio=self.__anio,
                km=self.__km
            )
        )
        return d