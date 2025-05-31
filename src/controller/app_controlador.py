from src.model.diccionario_file import DiccionarioFile
from src.model.diccionario_db import Consulta
from src.model.bitacora import Bitacora

class AppControlador:
    def __init__(self):
        self.bitacora = Bitacora(DiccionarioFile())
        # self.bitacora = Bitacora(Consulta())
    
    def iniciar_sesion(self, email, contraseña):
        return self.bitacora.verificar_credenciales(email, contraseña)

    def registrar_usuario(self, nombre, email, contraseña):
        return self.bitacora.registrar_supervisor(nombre, email, contraseña)
