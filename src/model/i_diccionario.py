from abc import ABC

class IDiccionario(ABC):
    def obtener_usuarios(self, email: str, contraseña: str):
        pass
    def verificar_usuario(self, email: str, contraseña: str) -> bool:
        pass
    def registrar_usuario(self, nombre: str, email: str, contraseña: str) -> bool:
        pass