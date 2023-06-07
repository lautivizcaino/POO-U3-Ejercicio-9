from listaVehiculos import ListaVehiculos
from objectEncoder import ObjectEncoder
from menu import Menu
from datetime import datetime
def test():
    jsonF=ObjectEncoder()   
    lista=ListaVehiculos()
    diccionario=jsonF.leerJSONArchivo('vehiculos.json')
    lista=jsonF.decodificarDiccionario(diccionario)
    menu=Menu()
    menu.opciones(jsonF,lista)
    
if __name__=="__main__":
    test()