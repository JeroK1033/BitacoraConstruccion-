from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador

Builder.load_file("src/view/gui/kv/MainScreen.kv")

class MainScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador
    
    def abrir_pantalla_login(self):
        """
        Cambia a la pantalla de inicio de sesión.
        """
        self.manager.current = "LoginScreen"
    
    def abrir_pantalla_registro(self):
        """
        Cambia a la pantalla de registro.
        """
        self.manager.current = "RegisterScreen"
    
    def cerrar_aplicacion(self):
        """
        Cierra la aplicación.
        """
        exit()