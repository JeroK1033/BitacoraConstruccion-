from src.model.i_diccionario import IDiccionario
from src.model.errores import ErrorCamposVacios


class Bitacora:
    """
    Representa la logica de la bitacora de construccion 
     
    """

    def __init__(self, diccionario: IDiccionario):
        self.__diccionario: IDiccionario = diccionario
    
    def inciar_sesion(self, email: str, contraseña: str) -> bool:
        """
        Verifica si el supervisor existe e incia sesion.
        
        """
        return self.__diccionario.verificar_usuario(email, contraseña)

    def registrar_usuario_nuevo(self, email: str, contraseña: str) -> bool:
        """
        Registra un nuevo usuario en la bitacora.
        
        """
        return self.__diccionario.registrar_usuario(email, contraseña)

    

    
    