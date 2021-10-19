from .proveedor import Proveedor
import json


class Proveedores :
    def __init__(self) :
        self.__proveedores = []

    def agregar(self, proveedor:Proveedor) :
        self.__proveedores.append(proveedor)

    def __str__(self) :
        return "".join(str(proveedor) + '\n' for proveedor in self.__proveedores)

    def guardar_archivo(self,ubicacion):
        
        try :
            with open(ubicacion, 'w') as archivo :
                lista =[proveedor.to_dict() for proveedor in self.__proveedores]
                json.dump(lista, archivo, indent=5)
                return 1
        except :
            return 0

    def abrir_archivo(self,ubicacion):

        try :
            with open(ubicacion, 'r') as archivo :
                lista = json.load(archivo)
                self.__proveedores = [Proveedor(**proveedor) for proveedor in lista]

                return 1
        except : 
            return 0

    def __iter__(self) :
        self.cont = 0
        return self

    def __next__(self) :
        if self.cont < len(self.__proveedores) :
            proveedor = self.__proveedores[self.cont]
            self.cont+=1 
            return proveedor
        else :
             raise StopIteration