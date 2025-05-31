from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador

Builder.load_file("src/view/gui/kv/RegisterScreen.kv")

class RegisterScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador
    
    def registrar_supervisor(self):
        nombre = self.ids.name_input.text
        email = self.ids.email_input.text
        contraseña = self.ids.password_input.text
        
        if not nombre or not email or not contraseña:
            self.ids.error.text = "Por favor, complete todos los campos."
            return
        
        if self.controlador.registrar_usuario(nombre, email, contraseña):
            self.ids.error.text = "Usuario registrado con éxito."
            self.manager.current = "LoginScreen"
        else:
            self.ids.error.text = "Supervisor ya registrado. Intente nuevamente."

    def volver(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "MainScreen"
