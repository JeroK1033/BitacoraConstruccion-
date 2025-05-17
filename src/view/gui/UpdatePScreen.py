from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador

Builder.load_file("src/view/gui/kv/UpdatePScreen.kv")

class UpdatePScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador.AppControlador = controlador
        
    
    def volver(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "HomeScreen"