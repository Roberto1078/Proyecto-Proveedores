class Proveedor :
    def __init__(self, nombre="",empresa="",direccion="",colonia="",telefono_de_oficina="",celular="",ciudad="",estado="",recomienda="",
                       correo_electronico="",link="",producto1="",producto2="",producto3="",producto4="",producto5="",producto6="",
                       oficio1="",oficio2="",oficio3="",oficio4="",oficio5="",oficio6="") :
                       self.__nombre = nombre
                       self.__empresa = empresa
                       self.__direccion = direccion
                       self.__colonia = colonia
                       self.__telefono_de_oficina = telefono_de_oficina
                       self.__celular = celular
                       self.__ciudad = ciudad
                       self.__estado = estado
                       self.__recomienda = recomienda
                       self.__correo_electronico = correo_electronico
                       self.__link = link
                       self.__producto1 = producto1
                       self.__producto2 = producto2
                       self.__producto3 = producto3
                       self.__producto4 = producto4
                       self.__producto5 = producto5
                       self.__producto6 = producto6
                       self.__oficio1 = oficio1
                       self.__oficio2 = oficio2
                       self.__oficio3 = oficio3
                       self.__oficio4 = oficio4
                       self.__oficio5 = oficio5
                       self.__oficio6 = oficio6

    def to_dict(self):
        return {
            'nombre' : self.__nombre,
            'empresa' : self.__empresa,
            'direccion' : self.__direccion,
            'colonia' : self.__colonia,
            'telefono_de_oficina' : self.__telefono_de_oficina,
            'celular' : self.__celular,
            'ciudad' : self.__ciudad,
            'estado' : self.__estado,
            'recomienda' : self.__recomienda,
            'correo_electronico' : self.__correo_electronico,
            'link' : self.__link,
            'producto1' : self.__producto1,
            'producto2' : self.__producto2,
            'producto3' : self.__producto3,
            'producto4' : self.__producto4,
            'producto5' : self.__producto5,
            'oficio1' : self.__oficio1,
            'oficio2' : self.__oficio2,
            'oficio3' : self.__oficio3,
            'oficio4' : self.__oficio4,
            'oficio5' : self.__oficio5,
            'oficio6' : self.__oficio6
        }
                  
    def __str__(self) :
        return ('Hola'
        )

    @property
    def nombre(self):
        return self.__nombre
    @property
    def empresa(self):
        return self.__empresa
    @property
    def direccion(self):
        return self.__direccion
    @property
    def colonia(self):
        return self.__colonia
    @property
    def telefono_de_oficina(self):
        return self.__telefono_de_oficina
    @property
    def celular(self):
        return self.__celular
    @property
    def ciudad(self):
        return self.__ciudad
    @property
    def estado(self):
        return self.__estado
    @property
    def recomienda(self):
        return self.__recomienda
    @property
    def correo_electronico(self):
        return self.__correo_electronico
    @property
    def link(self):
        return self.__link
    @property
    def producto1(self):
        return self.__producto1
    @property
    def producto2(self):
        return self.__producto2
    @property
    def producto3(self):
        return self.__producto3
    @property
    def producto4(self):
        return self.__producto4
    @property
    def producto5(self):
        return self.__producto5
    @property
    def producto6(self):
        return self.__producto6
    @property
    def oficio1(self):
        return self.__oficio1
    @property
    def oficio2(self):
        return self.__oficio2
    @property
    def oficio3(self):
        return self.__oficio3
    @property
    def oficio4(self):
        return self.__oficio4
    @property
    def oficio5(self):
        return self.__oficio5
    @property
    def oficio6(self):
        return self.__oficio6