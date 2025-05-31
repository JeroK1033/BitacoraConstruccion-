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
        self.supervisores: list[str] = self.___obtener_supervisores()
    
    def ___obtener_supervisores(self) -> list[str]:
        """
            Carga los supervisores desde el archivo ("assets/usuarios.txt")
            
            retuns:
                list[str]: Lista de usuarios cargadas desde el archivo.
        """
        supervisores = []
        
        with open("assets/usuarios.txt", "r") as file:
            for line in file:
                supervisores.append(line.strip().split(","))
        return supervisores
    
    

                    
                    