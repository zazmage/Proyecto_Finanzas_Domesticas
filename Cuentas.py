import Finanzas

class Cuenta():
    def __init__(self):
        self.__balance = 0
        self.__movimientos = None
    
    def realizar_movimiento(self):
        valor = int(input("Ingrese la cantidad de dinero: "))
        tipo = input("Ingrese el tipo de movimiento: ")
        descripcion = input("Ingrese una breve descripción: ")
        return valor, tipo, descripcion
    
    def get_balance(self):
        return self.__balance
    def get_movimientos(self):
        return self.__movimientos

class Persona(Cuenta):
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def realizar_movimiento(self, control):
        valor, tipo, descripcion = super().realizar_movimiento()
        movimiento = Finanzas.Movimiento(self.get_nombre(),valor,tipo,
                                         descripcion)
        control.lista_movimientos(movimiento)
        
    def get_nombre(self):
        return self.__nombre

class Casa(Cuenta):
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
