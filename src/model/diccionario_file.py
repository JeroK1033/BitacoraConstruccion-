from src.model.i_diccionario import IDiccionario
from datetime import datetime

class DiccionarioFile(IDiccionario):
    def __init__(self):
        self.supervisores = self._obtener_supervisores()
        self.actividades = self._obtener_actividades()

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
    
    def registrar_actividad(self, fecha_hora: datetime, supervisor: str, descripcion:str, anexo: str, condiciones_cliamticas:str) -> bool:
        self.actividades.append([fecha_hora.strftime("%Y-%m-%d %H:%M:%S"), supervisor, descripcion, anexo, condiciones_cliamticas])
        with open("assets/actividades.txt", "a") as file:
            file.write(f"{fecha_hora.strftime('%Y-%m-%d %H:%M:%S')},{supervisor},{descripcion},{anexo},{condiciones_cliamticas}\n")
        return True
    
    def _obtener_actividades(self):
        actividades = []
        with open("assets/actividades.txt", "r") as file:
            for line in file:
                actividades.append(line.strip().split(","))
        return actividades
    
    def consultar_actividades(self) -> list:
        return self.actividades

    
    

                    
                    