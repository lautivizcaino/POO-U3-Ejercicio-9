class Vehiculo:
    __marca:str
    __modelo:str
    __cantidadPuertas:int
    __color:str
    __precioBase:float
    def __init__(self,marca,modelo,puertas,color,precio) -> None:
        self.__marca=marca
        self.__modelo=modelo
        self.__cantidadPuertas=puertas
        self.__color=color
        self.__precioBase=precio
    def __str__(self) -> str:
        return'Marca:%s Modelo:%s Puertas:%s Color:%s Precio Base:%s '%(self.__marca,self.__modelo,self.__cantidadPuertas,self.__color,self.__precioBase)
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.__marca,
                modelo=self.__modelo,
                cantidadPuertas=self.__cantidadPuertas,
                color=self.__color,
                precioBase=self.__precioBase
            )
        )
        return d
    
    def getPrecio(self):
        return self.__precioBase
    def setPrecio(self,precio):
        self.__precioBase=precio
    def getPuertas(self):
        return self.__cantidadPuertas
    def getModelo(self):
        return self.__modelo
    def getMarca(self):
        return self.__marca
    def getColor(self):
        return self.__color