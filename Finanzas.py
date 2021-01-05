import Cuentas
class Movimiento():
    def __init__(self, usuario, valor, tipo, descripcion):
        self.__valor = valor
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__usuario = usuario
    
    def get_valor(self):
        return self.__valor
    def get_tipo(self):
        return self.__tipo
    def get_descripcion(self):
        return self.__descripcion
    def get_usuario(self):
        return self.__usuario

class Control_Finanzas():
    def __init__(self):
        self.__movimientos = []
    
    def lista_movimientos(self,movimiento):
        self.__movimientos.append(movimiento)
    
    def get_movimientos(self):
        return self.__movimientos