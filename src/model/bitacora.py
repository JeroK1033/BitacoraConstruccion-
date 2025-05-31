from src.model.i_diccionario import IDiccionario
from src.model.errores import ErrorCamposVacios


class Bitacora:
    """
    Representa la logica de la bitacora de construccion 
     
    """

    def __init__(self, diccionario: IDiccionario):
        self.__diccionario: IDiccionario = diccionario
    
    def verificar_supervisor(self, email: str, contraseña: str) -> bool:
        """
        Verifica si un supervisor existe en el archivo de texto.

        Args:
            email (str): El correo electrónico del usuario.
            contraseña (str): La contraseña del usuario.

        Returns:
            bool: True si el usuario existe, False en caso contrario.
        """
        for usuario in self.supervisores:
            if usuario[1] == email and usuario[2] == contraseña:
                return True
        return False

    def registrar_supervisor(self, nombre: str, email: str, contraseña: str) -> bool:
        """
        Registra un nuevo supervisor en el archivo de texto.
        Atributes:
            nombre (str): _description_
            email (str): _description_
            contrase (_type_): _description_

        Returns:
            bool: true si el supervisor fue registrado correctamente, false si ya existe.
        """
        for usuario in self.supervisores:
            if usuario[1] == email:
                return False 
            
        self.supervisores.append([nombre, email, contraseña])

        with open("assets/usuarios.txt", "a") as file:
            file.write(f"{nombre},{email},{contraseña}\n")

        return True

    

    
    