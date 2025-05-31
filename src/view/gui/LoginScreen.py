from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador


Builder.load_file("src/view/gui/kv/LoginScreen.kv")

class LoginScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador
           
    def iniciar_sesion(self):
        if self.controlador.iniciar_sesion(self.ids.email_input.text, self.ids.password_input.text):
            self.manager.current = "HomeScreen"
        else:
            self.ids.error_label.text = "Credenciales incorrectas. Inténtalo de nuevo."

    
    
    def volver(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "MainScreen"