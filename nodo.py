from vehiculo import Vehiculo
class Nodo:
    __vehiculo:Vehiculo
    __siguiente:object
    def __init__(self,vehiculo) -> None:
        self.__vehiculo=vehiculo
        self.__siguiente=None
    def getVehiculo(self):
        return self.__vehiculo
    def getSiguiente(self):
        return self.__siguiente
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
