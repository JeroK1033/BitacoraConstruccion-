from src.model.i_diccionario import IDiccionario

class DiccionarioFile(IDiccionario):
    def __init__(self):
        self.supervisores = self._obtener_supervisores()

    def _obtener_supervisores(self):
        supervisores = []
        with open("assets/usuarios.txt", "r") as file:
            for line in file:
                supervisores.append(line.strip().split(","))
        return supervisores

    def verificar_supervisor(self, email: str, contraseña: str) -> bool:
        for usuario in self.supervisores:
            if len(usuario) >= 3 and usuario[1] == email and usuario[2] == contraseña:
                return True
        return False

    def registrar_supervisor(self, nombre: str, email: str, contraseña: str) -> bool:
        for usuario in self.supervisores:
            if usuario[1] == email:
                return False  
        self.supervisores.append([nombre, email, contraseña])
        
        with open("assets/usuarios.txt", "a") as file:
            file.write(f"{nombre},{email},{contraseña}\n")

        return True

    
    

                    
                    