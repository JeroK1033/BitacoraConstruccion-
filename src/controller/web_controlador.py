from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.model.bitacora import Bitacora
from src.model.diccionario_file import DiccionarioFile

class CorreoInput(BaseModel):
    correo: str

class ContrasenaInput(BaseModel):
    contrasena: str



class WebControlador:
    def __init__(self):
        self.router = APIRouter(prefix="/api/v1")
        self.bitacora = Bitacora(DiccionarioFile())
        self.__registrar_rutas()
    
    def __registrar_rutas(self):
        @self.router.post("/usuarios")
        def registrar_usuario():
            return{"Usuario registrado exitosamente": self.bitacora.registrar_supervisor()}
        
        self.router.post("/IniciarSesion")
        def iniciar_sesion():
            return {"Iniciar sesion": self.bitacora.verificar_supervisor()}
