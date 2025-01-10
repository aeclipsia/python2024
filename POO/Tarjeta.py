class Tarjeta():
    comision=0.5;
    def __init__(self,id,saldo=1000):
        self.__id=id
        self.__saldo=saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,v):
        self.__saldo=v
        
    @property
    def id(self):
        return self.__id
        
    # def consultarSaldo(self):
    #     return self.__saldo
    
    def ingresar(self,cantidad):
        self.__saldo+=cantidad
        
    def reintegrar(self,cantidad):
        if (cantidad + cantidad * Tarjeta.comision > self.__saldo):
            return False
        self.__saldo-=cantidad+cantidad*Tarjeta.comision
        
    def __str__(self) -> str:
        return "Identificador: "+ str(self.id)