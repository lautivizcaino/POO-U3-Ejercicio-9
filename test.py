from listaVehiculos import ListaVehiculos
from nodo import Nodo
from nuevo import Nuevo
from usado import Usado
import unittest
class TestListaVehiculos(unittest.TestCase):
    def setUp(self) -> None:
        self.__lista=ListaVehiculos()
        unNuevo=Nuevo('Toyota','Corolla',5,'Blanco',20000.0,'base')
        self.__lista.agregarVehiculo(unNuevo)
        unUsado=Usado('Chevrolet','Corsa',3,'Azul',15000.0,'AAA123',2020,5000)
        self.__lista.agregarVehiculo(unUsado)

    def test__insertarElemento0(self):
        unNuevo=Nuevo('Toyota','Hilux',4,'Gris',25000.0,'full')
        self.__lista.insertarElemento(0,unNuevo)
        self.assertEqual(self.__lista.getNombres(),['Hilux','Corsa','Corolla'])
    def test__insertarElementoIntermedio(self):
        unUsado=Usado('Fiat','Palio',3,'Verde',10000.0,'CCC321',2012,4000)
        self.__lista.insertarElemento(1,unUsado)
        self.assertEqual(self.__lista.getNombres(),['Corsa','Palio','Corolla'])
    def test__insertarElementoFinal(self):
        otroNuevo=Nuevo('Toyota','Etios',5,'Negro',30000.0,'base')
        self.__lista.insertarElemento(2,otroNuevo)
        self.assertEqual(self.__lista.getNombres(),['Corsa','Corolla','Etios'])



    def test__agregarElementoFinal(self):
        unNuevo=Nuevo('Toyota','Hilux',4,'Gris',25000.0,'full')
        self.__lista.agregarElementoFinal(unNuevo)
        self.assertEqual(self.__lista.getNombres(),['Corsa','Corolla','Hilux'])



    def test__mostrarElemento0(self):
        unNuevo=Nuevo('Toyota','Hilux',4,'Gris',25000.0,'full')
        self.__lista.agregarVehiculo(unNuevo)
        vehiculo=self.__lista.mostrarElemento(0)
        self.assertEqual(vehiculo.getModelo(),'Hilux')
    def test__mostrarElementoIntermedio(self):
        unUsado=Usado('Fiat','Palio',3,'Verde',10000.0,'CCC321',2012,4000)
        self.__lista.agregarVehiculo(unUsado)
        vehiculo=self.__lista.mostrarElemento(1)
        self.assertEqual(vehiculo.getModelo(),'Corsa')
    def test__mostrarElementoFinal(self):
        otroNuevo=Nuevo('Toyota','Etios',5,'Negro',30000.0,'base')
        self.__lista.agregarVehiculo(otroNuevo)
        vehiculo=self.__lista.mostrarElemento(2)
        self.assertEqual(vehiculo.getModelo(),'Corolla')



    def test__mostrarPrecio(self):
        precioVenta=self.__lista.mostrarPrecio('AAA123',2018)
        self.assertEqual(precioVenta,1957.46)



if __name__=="__main__":
    unittest.main()