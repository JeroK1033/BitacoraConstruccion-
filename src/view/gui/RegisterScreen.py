from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador

Builder.load_file("src/view/gui/kv/RegisterScreen.kv")

class RegisterScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador.AppControlador = controlador
    
    def volver(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "MainScreen"