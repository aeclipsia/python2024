class Contacto:
    def __init__(self, nombre, tel, email):
        self.__nombre=nombre
        self.__tel=tel
        self.__email=email
        
    @property
    def tel(self):
        return self.__tel

class Agenda:
    def __init__(self):
        self.__contactos=[]

    def add(self, nombre, tel, email):
        for contacto in self.__contactos:
            if contacto.tel == tel:
                tel_existe=True
                
        if tel_existe:
            return False
        else:
            nuevo_contacto=Contacto(nombre,tel,email)
            self.__contactos.append(nuevo_contacto)
            return True
            
    def buscar(self, nombre="", tel="", email=""):
        for contacto in self.__contactos:
            if contacto.nombre == nombre or contacto.tel == tel or contacto.email == email:
                return contacto
        return False
    
    def eliminar(self, tel):
        for contacto in self.__contactos:
            if contacto.tel == tel:
                self.__contactos.remove(contacto)
                return True
        return False
    
    def __str__(self) -> str:
        if not self.__contactos:
            return ("La lista está vacía")
        else:
            return self.__contactos