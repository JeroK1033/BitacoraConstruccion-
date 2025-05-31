from abc import ABC, abstractmethod

class IDiccionario(ABC):

    @abstractmethod
    def verificar_supervisor(self, email: str, contraseña: str) -> bool:
        pass

    @abstractmethod
    def registrar_supervisor(self, nombre: str, email: str, contraseña: str) -> bool:
        pass
