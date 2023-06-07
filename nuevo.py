from vehiculo import Vehiculo
class Nuevo(Vehiculo):
    __version:str
    def __init__(self, marca, modelo, cantidadPuertas, color, precioBase,version) -> None:
        super().__init__(marca, modelo, cantidadPuertas, color, precioBase)
        self.__version=version
    def __str__(self) -> str:
        return super().__str__() + 'Version:%s'%self.__version
    def getVenta(self):
        importe=self.getPrecio()+self.getPrecio()*0.10
        if self.__version.upper()=='BASE':
            importe-=self.getPrecio()*2*0.01
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
                version=self.__version
            )
        )
        return d