from src.model.i_diccionario import IDiccionario
from src.model.errores import ErrorCamposVacios


class Bitacora:
    """
    Representa la logica de la bitacora de construccion 
     
    """
    def __init__(self, diccionario: IDiccionario):
        self.__diccionario= diccionario

    def verificar_credenciales(self, email:str, contraseña:str) -> bool:
        if not email or not contraseña:
            raise ErrorCamposVacios("Email y contraseña son obligatorios")
        return self.__diccionario.verificar_supervisor(email, contraseña)
    
    def registrar_supervisor(self, nombre:str, email:str, contraseña:str) -> bool:
        if not nombre or not email or not contraseña:
            raise ErrorCamposVacios("Todos los campos son obligatorios")
        return self.__diccionario.registrar_supervisor(nombre, email, contraseña)
        

    

    
    