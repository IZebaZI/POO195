class ExcepcionEdadInvalida(Exception):
    def _init_(self, edad, mensaje="La edad ingresada es menor a 18"):
        self.edad = edad
        self.mensaje = mensaje
        super()._init_(self.mensaje)
        print("La edad introducida fue",edad)

class ExcepcionNombre(Exception):
    def _init_(self, mensaje="El nombre no se encontro en la lista"):
        self.mensaje = mensaje
        super()._init_(self.mensaje)


class Controller:
    
    lista = ["emiliano"]

    def verificarEdadCont(self,edad):
        
        if edad < 18:
            raise ExcepcionEdadInvalida(edad)
        else:
            return 1
    
    
    def buscarNombre(self,nombre):
        
        if nombre in self.lista:
            return 1
        else:
            raise ExcepcionNombre