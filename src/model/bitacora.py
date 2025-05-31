from src.model.i_diccionario import IDiccionario
from src.model.errorres_usuario import ErrorCamposIncompletos, ErrorContraseñaCorta, ErrorEmailNo

class Bitacora:
    """
    Representa la logica de la bitacora de construccion 
     
    """
    def __init__(self, diccionario: IDiccionario):
        self.__diccionario= diccionario

    def verificar_credenciales(self, email:str, contraseña:str) -> bool:
        if not email or not contraseña:
            raise ErrorCamposIncompletos("Email y contraseña son obligatorios")
        return self.__diccionario.verificar_supervisor(email, contraseña)
    
    def registrar_supervisor(self, nombre:str, email:str, contraseña:str) -> bool:
        if not nombre or not email or not contraseña:
            raise ErrorCamposIncompletos("Todos los campos son obligatorios")
        else:
            if len(contraseña) < 8:
                raise ErrorContraseñaCorta("La contraseña debe tener al menos 8 caracteres")
            if '@' not in email or '.' not in email:
                raise ErrorEmailNo("El email debe ser válido")
        return self.__diccionario.registrar_supervisor(nombre, email, contraseña)

    def registrar_actividad(self, fecha_hora, supervisor, descripcion, anexo, condiciones_climaticas) -> bool:
        if not fecha_hora or not supervisor or not descripcion or not anexo or not condiciones_climaticas:
            raise ErrorCamposIncompletos("Todos los campos son obligatorios")
        return self.__diccionario.registrar_actividad(fecha_hora, supervisor, descripcion, anexo, condiciones_climaticas)
        

    

    
    