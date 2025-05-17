from abc import ABC

class IDiccionario(ABC):
    def __obtener_usuarios(self, email: str, contraseña: str):
        pass
    def __verificar_usuario(self, email: str, contraseña: str) -> bool:
        pass
    def __registrar_usuario(self, nombre: str, email: str, contraseña: str) -> bool:
        pass