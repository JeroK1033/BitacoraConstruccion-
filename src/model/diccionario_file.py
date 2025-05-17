from src.model.i_diccionario import IDiccionario

class DiccionarioFile(IDiccionario):
    """
        Clase que representa un diccionario de supervisores.
        
        Atributtes:
            usuarios (list[str]): Lista de supervisores cargados desde un archivo de texto.
    """

    def __init__(self):
        """
            Inicializa una instancia de la clase DiccionarioFile, cargando los usuarios desde un archivo de texto.
        """
        self.usuarios: list[str] = self.cargar_usuarios()
    
    def __obtener_supervisores(self) -> list[str]:
        """
            Carga los supervisores desde el archivo ("assets/usuarios.txt")
            
            retuns:
                list[str]: Lista de usuarios cargadas desde el archivo, eliminando espacios en blanco, saltos de línea y dividiendo el texto por comas.
        """
        usuarios = []
        
        with open("assets/usuarios.txt", "r") as file:
            for line in file:
                usuarios.append(line.strip().split(","))
        return usuarios
    
    def __verificar_supervisor(self, email: str, contraseña: str) -> bool:
        """
        Verifica si un supervisor existe en el archivo de texto.

        Args:
            email (str): El correo electrónico del usuario.
            contraseña (str): La contraseña del usuario.

        Returns:
            bool: True si el usuario existe, False en caso contrario.
        """
        for usuario in self.usuarios:
            if len(usuario) >= 2 and usuario[0] == email and usuario[1] == contraseña:
                return True
        return False

    
    def __registrar_supervisor(self, nombre: str, email: str, contraseña: str) -> bool:
        """
        Registra un nuevo supervisor en el archivo de texto, pero primero verifica si el usuario ya existe.

        Args:
            nombre (str): _description_
            email (str): _description_
            contrase (_type_): _description_

        Returns:
            bool: true si el supervisor fue registrado correctamente, false si ya existe.
        """
        for usuario in self.usuarios:
            if usuario[1] == email:
                return False 
            
        self.usuarios.append([nombre, email, contraseña])

        with open("assets/usuarios.txt", "a") as file:
            file.write(f"{nombre},{email},{contraseña}\n")

        return True


                    
                    